from aiohttp import web
from aiomisc.log import basic_config

from cv.server.app import create_app


def main():
    app = create_app()
    basic_config(app["config"].LOG_LEVEL, app["config"].LOG_FORMAT)

    web.run_app(app, host=app["config"].HTTP_ADDRESS, port=app["config"].HTTP_PORT)
