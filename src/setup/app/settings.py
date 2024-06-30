from argparse import ArgumentParser

from config.settings.manager.base import SettingsManager

__all__ = [
    'configure_settings'
]


def configure_settings(settings_manager: SettingsManager, parser: ArgumentParser):
    args = parser.parse_args()
    settings_manager.set_settings(args.settings)
