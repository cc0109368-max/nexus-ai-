from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, ConfigDict
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import current_user
from app.auth.models import Organization, OrganizationMember, User
from app.db.session import get_db

router = APIRouter(prefix="/organizations", tags=["organizations"])


class OrganizationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    name: str
    slug: str


@router.get("/{organization_id}", response_model=OrganizationResponse)
async def get_organization(
    organization_id: UUID,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
) -> Organization:
    membership = await db.scalar(
        select(OrganizationMember).where(
            OrganizationMember.organization_id == organization_id,
            OrganizationMember.user_id == user.id,
        )
    )
    if membership is None:
        # Do not disclose whether another tenant's organization exists.
        raise HTTPException(status_code=404, detail="Organization not found")
    organization = await db.get(Organization, organization_id)
    if organization is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    return organization
