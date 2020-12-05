from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import os
import pwd

from aiomisc.log import LogFormat, basic_config
from configargparse import ArgumentParser
from yarl import URL

from cv.utils.pg import DEFAULT_PG_URL


def read_args_from_env() -> ArgumentParser:
    parser = ArgumentParser(
        auto_env_var_prefix='LANDING_',
        formatter_class=ArgumentDefaultsHelpFormatter,
        default_config_files=[
            os.path.join(os.path.expanduser('~'), '.landing'),
            '/etc/landing.conf',
        ],
    )

    parser.add_argument('--user', required=False, type=pwd.getpwnam, help='Change process UID')

    group = parser.add_argument_group('HTTP Options')
    group.add_argument('--http-address', default='0.0.0.0')
    group.add_argument('--http-port', type=int, default=8088)

    group = parser.add_argument_group('PostgreSQL options')
    group.add_argument('--pg-url', type=URL, default=DEFAULT_PG_URL)
    group.add_argument('--pg-pool-min-size', type=int, default=10)
    group.add_argument('--pg-pool-max-size', type=int, default=10)

    group = parser.add_argument_group('Logging options')
    group.add_argument('--log-level', default='info',
                       choices=('debug', 'info', 'warning', 'error', 'fatal'))
    group.add_argument('--log-format', choices=LogFormat.choices(),
                       default='color')

    return parser
