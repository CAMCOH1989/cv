from pathlib import Path

from aiohttp.web import Application, View, Response
from asyncpgsa import PG
from jinja2 import FileSystemLoader, Environment

from cv.utils.config import Config


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

    @property
    def config(self) -> Config:
        return self.request.app["config"]

    @property
    async def locale(self) -> str:
        return dict(self.request.rel_url.query).get("locale", "ru")
