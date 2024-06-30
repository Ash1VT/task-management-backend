from typing import Optional

from config.settings.manager.base import SettingsManager
from config.settings.server import ServerSettings, DevelopServerSettings, TestServerSettings, ProductionServerSettings

__all__ = [
    'ServerSettingsManager'
]


class ServerSettingsManager(SettingsManager[ServerSettings]):
    _settings: Optional[ServerSettings] = None
    _settings_map = {
        'dev': DevelopServerSettings,
        'test': TestServerSettings,
        'prod': ProductionServerSettings
    }
