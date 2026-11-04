from uuid import uuid4

from app.auth.security import (
    create_access_token,
    decode_access_token,
    hash_password,
    verify_password,
)


def test_password_hash_round_trip() -> None:
    password = "correct horse battery staple"
    hashed = hash_password(password)
    assert hashed != password
    assert verify_password(password, hashed)
    assert not verify_password("incorrect password", hashed)


def test_access_token_round_trip() -> None:
    user_id = uuid4()
    token, expires_in = create_access_token(user_id)
    assert expires_in > 0
    assert decode_access_token(token) == user_id
