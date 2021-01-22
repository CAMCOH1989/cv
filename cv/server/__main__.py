from aiohttp import web
from aiomisc.log import basic_config

from cv.server.app import create_app
from cv.utils.config import config


def main():
    basic_config(config.LOG_LEVEL, config.LOG_FORMAT)

    app = create_app()
    web.run_app(app, host=config.HTTP_ADDRESS, port=config.HTTP_PORT)
