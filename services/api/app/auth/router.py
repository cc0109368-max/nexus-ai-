import re
import unicodedata
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.models import Organization, OrganizationMember, User
from app.auth.schemas import AuthResponse, LoginRequest, RegisterRequest
from app.auth.security import create_access_token, hash_password, verify_password
from app.db.session import get_db

router = APIRouter(prefix="/auth", tags=["authentication"])


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().lower()
    base = re.sub(r"[^a-z0-9]+", "-", normalized).strip("-") or "workspace"
    return base[:150]


async def build_auth_response(user: User, organization: Organization) -> AuthResponse:
    token, expires_in = create_access_token(user.id)
    return AuthResponse(
        access_token=token,
        expires_in=expires_in,
        user=user,
        organization=organization,
    )


@router.post("/register", response_model=AuthResponse, status_code=status.HTTP_201_CREATED)
async def register(payload: RegisterRequest, db: AsyncSession = Depends(get_db)) -> AuthResponse:
    email = str(payload.email).lower()
    existing = await db.scalar(select(User).where(User.email == email))
    if existing:
        raise HTTPException(status_code=409, detail="An account with this email already exists")

    user = User(
        email=email,
        full_name=payload.full_name.strip(),
        password_hash=hash_password(payload.password),
    )
    organization = Organization(
        name=payload.organization_name.strip(),
        slug=f"{slugify(payload.organization_name)}-{uuid4().hex[:8]}",
    )
    try:
        db.add_all([user, organization])
        await db.flush()
        db.add(OrganizationMember(user_id=user.id, organization_id=organization.id, role="owner"))
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=409, detail="An account with this email already exists") from None
    await db.refresh(user)
    await db.refresh(organization)
    return await build_auth_response(user, organization)


@router.post("/login", response_model=AuthResponse)
async def login(payload: LoginRequest, db: AsyncSession = Depends(get_db)) -> AuthResponse:
    email = str(payload.email).lower()
    user = await db.scalar(select(User).where(User.email == email, User.is_active.is_(True)))
    if user is None or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    membership = await db.scalar(
        select(OrganizationMember)
        .where(OrganizationMember.user_id == user.id)
        .order_by(OrganizationMember.created_at)
    )
    if membership is None:
        raise HTTPException(status_code=403, detail="No organization membership is configured")
    organization = await db.get(Organization, membership.organization_id)
    if organization is None:
        raise HTTPException(status_code=403, detail="Organization is unavailable")
    return await build_auth_response(user, organization)
