from functools import partial
from pathlib import Path

from aiohttp.web import Application

from cv.utils.pg import setup_app_pg
from cv.server.handlers.skills_handler import SkillsView
from cv.server.handlers.cv_handler import CVView
from cv.server.handlers.statistics_handler import StatisticsView
from cv.utils.config import config
from cv.server.middlewears import check_cookies


STATIC_PATH = Path(__file__).parent.parent / 'server/templates/static'


def create_app() -> Application:
    app = Application(
        client_max_size=20 * 1024 * 1024,
        middlewares=[check_cookies]
    )
    app["config"] = config

    app.cleanup_ctx.append(partial(setup_app_pg, args=config))

    app.router.add_route('GET', '/api/skills', SkillsView)
    app.router.add_route('GET', '/api/cv', CVView)
    app.router.add_route('*', '/api/statistics', StatisticsView)
    app.router.add_route('POST', '/admin/skills', SkillsView)

    return app
