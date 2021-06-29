import uvicorn
from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html
)

from starlette.middleware.cors import CORSMiddleware

from backend.app.core.config import settings
from backend.app.api.routers import api_router


app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    openapi_url=f'{settings.BASE_API}/openapi.json',
    openapi_tags=settings.OPENAPI_TAGS,
    docs_url=None,
    redoc_url=None
)

app.mount('/static', StaticFiles(directory=rf'{Path(__file__).parent}\static'), name='static')

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )


@app.get('/docs', include_in_schema=False)
async def swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + ' - Swagger UI',
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_favicon_url=settings.FAVICON,
    )


@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()


@app.get('/redoc', include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + ' - ReDoc',
        redoc_favicon_url=settings.FAVICON,
    )


app.include_router(api_router, prefix=settings.BASE_API)


if __name__ == '__main__':
    uvicorn.run('main:app', host=settings.HOST, port=settings.PORT, debug=settings.ENV == 'dev')
