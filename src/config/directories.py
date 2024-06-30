from pathlib import Path

__all__ = [
    'SRC_DIRECTORY',
    'BASE_DIRECTORY',
    'ENV_DIRECTORY'
]

SRC_DIRECTORY = Path(__file__).resolve().parent.parent
BASE_DIRECTORY = SRC_DIRECTORY.parent
ENV_DIRECTORY = BASE_DIRECTORY / 'env'
