from pydantic import ValidationError
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt, ExpiredSignatureError

from backend.app.core.config import config
from backend.app.crud.access import get_user_info
from backend.app.schemas.access import TokenPayload


OAUTH_SCHEME = OAuth2PasswordBearer(tokenUrl=f'{config.BASE_API}/login')


async def get_current_user(token: str = Depends(OAUTH_SCHEME)):
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
        token_payload = TokenPayload(**payload)
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Token expired'
        )
    except (JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Invalid token'
        )
    else:
        return get_user_info(token_payload.sub)
