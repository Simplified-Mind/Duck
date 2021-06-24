import os
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html
)

from starlette.middleware.cors import CORSMiddleware

from backend.app.core.config import config
from backend.app.api.routers import api_router


app = FastAPI(
    title=config.PROJECT_NAME,
    description=config.DESCRIPTION,
    version=config.VERSION,
    openapi_url=f'{config.BASE_API}/openapi.json',
    openapi_tags=config.OPENAPI_TAGS,
    docs_url=None,
    redoc_url=None
)

app.mount('/static', StaticFiles(directory=os.path.join(os.path.dirname(__file__), 'static')), name='static')

if config.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in config.BACKEND_CORS_ORIGINS],
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
        swagger_favicon_url=config.FAVICON,
    )


@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()


@app.get('/redoc', include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + ' - ReDoc',
        redoc_favicon_url=config.FAVICON,
    )


app.include_router(api_router, prefix=config.BASE_API)


if __name__ == '__main__':
    uvicorn.run('main:app', host=config.HOST, port=config.PORT, debug=config.ENV == 'dev')
