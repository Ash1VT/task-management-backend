from abc import ABC

from pydantic_settings import BaseSettings, SettingsConfigDict

from config.directories import ENV_DIRECTORY
from config.settings.db import PostgresSqlSettings, SqliteSettings

__all__ = [
    'ServerSettings',
    'DevelopServerSettings',
    'TestServerSettings',
    'ProductionServerSettings'
]


class ServerSettings(BaseSettings, ABC):
    web_app_host: str
    web_app_port: int
    reload: bool


class DevelopServerSettings(ServerSettings, PostgresSqlSettings):
    reload: bool = True

    model_config = SettingsConfigDict(env_file=ENV_DIRECTORY / '.env.dev')


class TestServerSettings(ServerSettings, SqliteSettings):
    reload: bool = False

    model_config = SettingsConfigDict(env_file=ENV_DIRECTORY / '.env.test')


class ProductionServerSettings(ServerSettings, PostgresSqlSettings):
    reload: bool = False

    model_config = SettingsConfigDict(env_file=ENV_DIRECTORY / '.env.prod')
