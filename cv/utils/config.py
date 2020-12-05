import os
from pathlib import Path

from yaml import load, SafeLoader


def _service_path(folder: str, filename: str) -> str:
    current_directory = os.path.dirname(os.path.realpath(__file__))
    return os.path.normpath(os.path.join(current_directory, "..", folder, filename))


def load_config() -> dict:
    config_file_path = Path(__file__).parent.parent / "config/config.yml"
    with open(config_file_path, "r") as f:
        data = f.read()
        config_dict = load(data, SafeLoader)
        return config_dict


class Config:
    conf = load_config()
    if conf is None:
        conf = dict()

    # Server config
    BASE_URL = conf.get("BASE_URL", "http://cv.local")
    HTTP_PORT = conf.get("HTTP_PORT", 8099)
    STATIC_PATH = conf.get("STATIC_PATH", Path(__file__).parent.parent / "templates/static")
    TEMPLATES_PATH = conf.get("STATIC_PATH", Path(__file__).parent.parent / "templates")
    LOG_LEVEL = conf.get("LOG_LEVEL", "info")
    LOG_FORMAT = conf.get("LOG_FORMAT", "color")
    WEB_SECURE_COOKIES = conf.get("WEB_SECURE_COOKIES", False)

    # Database config
    DEFAULT_PG_URL = conf.get("PDB_URL", "postgresql://api:hackme@127.0.0.1:5488/app_sharer")
    PG_POOL_MIN_SIZE = conf.get("PG_POOL_MIN_SIZE", 10)
    PG_POOL_MAX_SIZE = conf.get("PG_POOL_MAX_SIZE", 10)


config = Config()
