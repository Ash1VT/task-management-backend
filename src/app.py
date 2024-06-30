from config.args import parser
from config.cors import origins
from setup.app.app import start_app, app
from setup.app.cors import configure_cors
from setup.app.settings import configure_settings
from setup.settings import server_settings_manager

if __name__ == "__main__":
    configure_settings(server_settings_manager, parser)
    configure_cors(app, origins=origins)

    server_settings = server_settings_manager.get_settings()
    start_app(server_settings)
