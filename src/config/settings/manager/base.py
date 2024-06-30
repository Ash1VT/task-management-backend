from abc import ABC, abstractmethod
from typing import Dict, Type, Optional

from pydantic_settings import BaseSettings

__all__ = [
    'SettingsManager'
]


class SettingsManager[T: BaseSettings](ABC):
    _settings: Optional[T] = None
    _settings_map: Dict[str, Type[T]] = {}

    def set_settings(self, settings_name: str):
        try:
            settings_class = self._settings_map[settings_name]
        except KeyError:
            raise ValueError(f'Invalid server settings name "{settings_name}".'
                             f' Available names: {self._settings_map.keys()}')
        self._settings = settings_class()

    def get_settings(self) -> T:
        if self._settings is None:
            raise ValueError('Settings are not set')

        return self._settings
