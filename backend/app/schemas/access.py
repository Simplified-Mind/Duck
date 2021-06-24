from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    name: str
    photo: str
    email: str
    display_name: str
    profile: dict


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: Optional[str] = None
