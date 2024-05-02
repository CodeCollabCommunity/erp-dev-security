import time

from fastapi import FastAPI, Request, WebSocket, requests
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from app.api import api_router

fastapi_app = FastAPI(
    title='security microservice',
    description='security microservice API',
    # docs_url=None, # Disable docs (Swagger UI)
    # redoc_url=None, # Disable redoc
    swagger_ui_parameters={'docExpansion': 'None'}
)

fastapi_app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins= ["*"],
    allow_methods= ["*"],
    allow_headers= ["*"]
)

@fastapi_app.get("/", status_code=200)
def healthcheck() -> dict:
    return {"Healthcheck": "Ok"}


fastapi_app.include_router(
    router=api_router,
    prefix='/api/v1'
)


# fastapi_app.mount(
#     '/statics', StaticFiles(directory=statics, html=True), name='statics'
# )
app = fastapi_app
