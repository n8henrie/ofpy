"""get_config.py
Imports the config for ofpy, or tries to create one and exits if it doesn't
exist yet.
"""


import os.path
import logging
import sys

try:
    from configparser import SafeConfigParser
except ImportError:
    from ConfigParser import SafeConfigParser

logging.basicConfig(
    level=logging.WARNING,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
    )


logger_name = str(__file__) + " :: " + str(__name__)
logger = logging.getLogger(logger_name)

# Defaults to ~/.ofpy_config
custom_config_dir = None


def make_config(config_path):
    default_config = '''# Config file for ofpy
# https://github.com/n8henrie/ofpy

[MAILDROP]
# Your OmniFocus Maildrop address
maildrop_address = example@sync.omnigroup.com

[EMAIL]
# Your email server info, defaults for Gmail
# Escape % in your password with another %
username = example@gmail.com
password = my_awesome_password
port = 587
server_address = smtp.gmail.com

[DROPBOX]
# The Dropbox folder that Hazel monitors
task_folder = ~/Dropbox

[EDITOR]
# Your preferred editor. If blank, will use your $EDITOR, or default to vim.
editor = vim
'''

    with open(config_path, 'w') as w:
        w.write(default_config)


def get_config():
    config = SafeConfigParser()

    try:
        custom_config_dir = os.path.expanduser(custom_config_dir)
        config_path = os.path.join(custom_config_dir, '.ofpy_config')
    except UnboundLocalError:
        home_dir = os.path.expanduser('~')
        config_path = os.path.join(home_dir, '.ofpy_config')

    if not os.path.exists(config_path):
        try:
            make_config(config_path)

        except Exception as e:
            logger.exception("It doesn't look like you have a config file, but"
                             " I wasn't able to create the template for you.")
        else:
            logger.warning('Config file did not exist, so I created a template'
                           ' at ~/.ofpy_config. Please edit with your config.')
            sys.exit(0)

    logger.debug("Parsing config file {}".format(config_path))
    with open(config_path) as r:
        try:
            config.read_file(r)
        except AttributeError:
            config.readfp(r)

    return config
