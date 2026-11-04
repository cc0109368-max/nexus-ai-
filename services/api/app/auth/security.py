from datetime import datetime, timedelta, timezone
from uuid import UUID

import jwt
from argon2 import PasswordHasher
from argon2.exceptions import VerificationError

from app.core.config import get_settings

_password_hasher = PasswordHasher()


def hash_password(password: str) -> str:
    return _password_hasher.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
    try:
        return _password_hasher.verify(password_hash, password)
    except VerificationError:
        return False


def create_access_token(user_id: UUID) -> tuple[str, int]:
    settings = get_settings()
    expires_in = settings.access_token_expire_minutes * 60
    now = datetime.now(timezone.utc)
    payload = {"sub": str(user_id), "iat": now, "exp": now + timedelta(seconds=expires_in)}
    token = jwt.encode(payload, settings.secret_key.get_secret_value(), algorithm="HS256")
    return token, expires_in


def decode_access_token(token: str) -> UUID:
    settings = get_settings()
    payload = jwt.decode(token, settings.secret_key.get_secret_value(), algorithms=["HS256"])
    return UUID(payload["sub"])
