import logging
import os

from aiohttp import web
from aiomisc.log import basic_config

from cv.server.app import create_app
from cv.utils.read_args import read_args_from_env


def main():
    args = read_args_from_env().parse_args()

    basic_config(args.log_level, args.log_format)

    if args.user is not None:
        logging.info('Changing user to %r', args.user.pw_name)
        os.setgid(args.user.pw_gid)
        os.setuid(args.user.pw_uid)

    app = create_app()
    web.run_app(app, host=args.http_address, port=args.http_port)
