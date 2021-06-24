from typing import Any
from fastapi import APIRouter

router = APIRouter()


@router.get('/fundamental')
def get() -> Any:
    pass
