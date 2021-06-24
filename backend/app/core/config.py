import secrets
from typing import Optional, List
from dataclasses import dataclass
from pydantic import AnyHttpUrl, BaseSettings


class Base(BaseSettings):
    PROJECT_NAME: Optional[str] = 'Analytics'
    VERSION: Optional[str] = '0.0.1'

    FAVICON: Optional[str] = '/static/favicon.ico'
    DESCRIPTION: Optional[str] = '''### Summary
    The API facilitates all required front end configurations.
    ©Analytics Team
    '''

    ALGORITHM: Optional[str] = 'HS256'
    SECRET_KEY: Optional[str] = secrets.token_urlsafe(256)

    # 60 minutes * 24 hours * 1 day = 1 day
    ACCESS_TOKEN_EXPIRE_MINUTES: Optional[int] = 60 * 24 * 1

    # e.g., ['http：//localhost']
    BACKEND_CORS_ORIGINS: Optional[List[AnyHttpUrl]] = []

    OPENAPI_TAGS: Optional[List[dict]] = [
        {
            'name': 'User Permission',
            'description': '[OAuth2 with Password (and hashing), Bearer with JWT tokens]'
                           '(https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#advanced-usage-with-scopes)'
        },
        {
            'name': 'Task',
            'description': 'Background Task',
        }
    ]


class Development(Base):
    BASE_API: str = '/dev-api/v1'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ['*']


class UAT(Base):
    BASE_API = '/uat-api/v1'


class Production(Base):
    BASE_API = '/prod-api/v1'


@dataclass
class Config:
    ENV: Optional[str] = 'dev'

    def __post_init__(self):
        options = {
            'dev': Development(),
            'uat': UAT(),
            'prod': Production()
        }
        self.__dict__.update(**options[self.ENV].__dict__)


config = Config()
