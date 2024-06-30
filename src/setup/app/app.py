from fastapi import FastAPI

from config.settings.server import ServerSettings

__all__ = [
    'app',
    'start_app'
]

app = FastAPI(
    title="Task Management System",
    version="0.0.1",
    description="Task Management System",
)


def start_app(settings: ServerSettings):
    import uvicorn
    uvicorn.run(app="setup.app.app:app", host=settings.web_app_host, port=settings.web_app_port, reload=settings.reload)
