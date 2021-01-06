from functools import partial
from pathlib import Path

from aiohttp.web import Application
from configargparse import Namespace

from cv.utils.pg import setup_app_pg
from cv.server.handlers.skills_handler import SkillsView
from cv.server.handlers.cv_handler import CVView
from cv.utils.config import config


STATIC_PATH = Path(__file__).parent.parent / 'server/templates/static'


def create_app() -> Application:
    app = Application(
        client_max_size=20 * 1024 * 1024,
    )

    app.cleanup_ctx.append(partial(setup_app_pg, args=config))

    app.router.add_route('GET', '/api/skills', SkillsView)
    app.router.add_route('GET', '/api/cv', CVView)

    return app
