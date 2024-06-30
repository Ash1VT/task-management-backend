from typing import List

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

__all__ = [
    'configure_cors'
]


def configure_cors(app: FastAPI, origins: List[str], allow_credentials: bool = True) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=allow_credentials,
        allow_methods=["*"],
        allow_headers=["*"],
    )
