from typing import Any
from datetime import timedelta

from fastapi.security import OAuth2PasswordRequestForm
from fastapi import status ,APIRouter, Depends, HTTPException

from backend.app.core.config import settings
from backend.app.crud.access import authenticate
from backend.app.api.deps import get_current_user
from backend.app.schemas.access import User, Token
from backend.app.core.security import create_access_token


router = APIRouter()


@router.post('/login', response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    subject = authenticate(form_data.username, form_data.password)

    if subject is False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid credentials',
            headers={'WWW-Authenticate': 'Bearer'}
        )
    else:
        expires_delta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        return {
            'access_token': create_access_token(subject, expires_delta),
            'token_type': 'bearer'
        }


@router.get('/logout', include_in_schema=False)
def logout() -> dict:
    return {}


@router.get('/user/info')
def get_user_info(current_user: User = Depends(get_current_user)) -> Any:
    return current_user
