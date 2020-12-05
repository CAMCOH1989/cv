import logging
import os
from pathlib import Path
from types import SimpleNamespace
from typing import Union

from aiohttp.web_app import Application
from alembic.config import Config
from asyncpgsa import PG
from configargparse import Namespace

from cv.utils.config import Config as cfg


CENSORED = '***'
DEFAULT_PG_URL = 'postgresql://api:hackme@localhost:5432/cv_db'
PROJECT_PATH = Path(__file__).parent.parent

log = logging.getLogger(__name__)


async def setup_pg(args):
    pg = PG()
    await pg.init(
        str(args.DEFAULT_PG_URL),
        min_size=args.PG_POOL_MIN_SIZE,
        max_size=args.PG_POOL_MAX_SIZE
    )
    return pg


async def setup_app_pg(app: Application, args: cfg) -> PG:
    db_info = args.DEFAULT_PG_URL
    log.info('Connecting to database: %s', db_info)

    app['pg'] = PG()
    await app['pg'].init(
        str(args.DEFAULT_PG_URL),
        min_size=args.PG_POOL_MIN_SIZE,
        max_size=args.PG_POOL_MAX_SIZE
    )
    await app['pg'].fetchval('SELECT 1')
    log.info('Connected to database %s', db_info)

    try:
        yield
    finally:
        log.info('Disconnecting from database %s', db_info)
        await app['pg'].pool.close()
        log.info('Disconnected from database %s', db_info)


def make_alembic_config(
        cmd_opts: Union[Namespace, SimpleNamespace],
        base_path: Path = PROJECT_PATH
) -> Config:
    if not os.path.isabs(cmd_opts.config):
        cmd_opts.config = str(base_path / cmd_opts.config)

    config = Config(
        file_=cmd_opts.config,
        ini_section=cmd_opts.name,
        cmd_opts=cmd_opts
    )

    # Подменяем путь alembic на абсолютный
    alembic_location = config.get_main_option('script_location')
    if not os.path.isabs(alembic_location):
        config.set_main_option(
            'script_location', str(base_path / alembic_location)
        )
    if cmd_opts.pg_url:
        config.set_main_option('sqlalchemy.url', cmd_opts.pg_url)

    return config
