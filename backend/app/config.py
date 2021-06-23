from typing import Optional
from dataclasses import dataclass


@dataclass
class Development:
    port: int = 9527
    base_api = '/dev-api'


@dataclass
class UAT:
    port: int = 9527
    base_api = '/uat-api'


@dataclass
class Production:
    port: int = 9527
    base_api = '/prod-api'


@dataclass
class Config:
    env: Optional[str] = 'dev'

    def __post_init__(self):
        options = {
            'dev': Development(),
            'uat': UAT(),
            'prod': Production()
        }
        self.__dict__.update(**options[self.env].__dict__)
