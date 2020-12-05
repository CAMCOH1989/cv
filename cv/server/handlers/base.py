from pathlib import Path

from aiohttp.web import Application, View, Response
from asyncpgsa import PG
from jinja2 import FileSystemLoader, Environment


class BaseView(View):
    TEMPLATES_PATH = Path(__file__).parent.parent / 'templates'

    @property
    def app(self) -> Application:
        return self.request.app

    @property
    def jinja_env(self) -> Environment:
        return Environment(loader=FileSystemLoader(self.TEMPLATES_PATH))

    @property
    def pg(self) -> PG:
        return self.request.app['pg']
