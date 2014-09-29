#! /usr/bin/env python3
'''n8of.py
A small module to add tasks to OmniFocus from my other non-Mac machines.

# Planned functionality:

- Will test for internet connectivity
- Given internet connectivity and a config, will email tasks to MailDrop
- Without internet connectivity, will add to a Dropbox folder, anticipating
the user will have Hazel and Dropbox add to OmniFocus.
'''

import sys
import internet_on
import get_config
import datetime
import os.path
import maildrop
import subprocess
import logging


logging.basicConfig(
    level=logging.WARNING,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger_name = str(__file__) + " :: " + str(__name__)
logger = logging.getLogger(logger_name)

logger.debug("Logging started.")


def internet_is_on():
    try:
        internet_on.internet_on()
        return True
    except:
        return False


def set_task_path(config):
    now = datetime.datetime.now()
    ts = now.strftime('%Y%m%dT%H%M%S')

    task_name = '{}.txt'.format(ts)
    task_folder = os.path.expanduser(config['DROPBOX']['task_folder'])
    task_path = os.path.join(task_folder, task_name)
    return task_path


def main():

    try:
        logger.debug("Getting config.")
        config = get_config.get_config()
    except Exception as e:
        logger.exception(e)
        logger.error('Config file problem.')

    logger.debug("sys.argv length: {}".format(len(sys.argv)))

    if len(sys.argv) == 1:
        # No arguments given with the script, so make a new task in editor.

        task_path = set_task_path(config)
        editor = config['EDITOR']['editor']

        logger.debug("Calling editor {} to path {}".format(editor, task_path))

        subprocess.call([editor, task_path])

    elif len(sys.argv) > 1:
        # Arguments given with script, so assume a one-liner. Email using
        # maildrop given an internet connection, otherwise write to a file as
        # per above.

        task_list = sys.argv[1:]
        task = ' '.join(task_list)

        if internet_is_on():
            logger.debug("Internet is on. Passing to maildrop:\ntask: "
                         "{}\nconfig:{}".format(task, config))
            maildrop.maildrop(task, config)
        else:
            logger.debug("Internet is off. Writing to file.")

            task_path = set_task_path(config)
            with open(task_path, 'w') as f:
                f.write(task)

if __name__ == '__main__':
    main()
