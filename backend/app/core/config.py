import secrets
from pathlib import Path
from base64 import b64encode
from typing import Optional, List
from dataclasses import dataclass
from pydantic import AnyHttpUrl, BaseSettings

FRONTEND_DIR = str(Path(__file__).parent).replace(r'backend\app\core', r'frontend')


class Base(BaseSettings):
    PROJECT_NAME: Optional[str] = 'Analytics'
    HOST: Optional[str] = '0.0.0.0'
    PORT: Optional[int] = 8888
    VERSION: Optional[str] = '0.0.1'
    FAVICON: Optional[str] = '/static/favicon.ico'
    DESCRIPTION: Optional[str] = '''### Overview
    The API facilitates all front end configurations.
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
            'description': '[Background Task](https://fastapi.tiangolo.com/tutorial/background-tasks/)',
        },
        {
            'name': 'Environmental',
            'description': 'Environmental'
        },
        {
            'name': 'Gas',
            'description': 'Gas'
        },
        {
            'name': 'LNG',
            'description': 'LNG'
        },
        {
            'name': 'Power',
            'description': 'Power'
        }
    ]

    ANONYMOUS: Optional[str] = b64encode(open(Path(rf'{FRONTEND_DIR}\public\anonymous.jpg'), 'rb').read())

    FRONTEND = {
        'home': '/',
        'logo': '',
        'favicon': '',
        'authentication': True,
        'internationalization': True,
        'api': {
            'environmental': {
                'fundamental': {}
            },
            'gas': {
                'fundamental': {}
            },
            'lng': {
                'fundamental': {}
            },
            'power': {
                'fundamental': {}
            }
        }
    }


class Development(Base):
    BASE_API: str = '/dev-api/v1'


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
