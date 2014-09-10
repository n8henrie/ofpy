#! /usr/bin/env python3
'''n8of.py
A little module that will help me add tasks to OmniFocus from my other non-Mac machines.

# Planned functionality:

- Will test for internet connectivity
- Given internet connectivity and a config, will email tasks to MailDrop
- Without internet connectivity, will add to a Dropbox folder, anticipating
the user will have Hazel and Dropbox add to OmniFocus.
'''

import sys
import internet_on
import get_config
import datetime # todo: datetime timestamp setup
import os.path
import maildrop
import logging
import subprocess

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
#    filename='/Users/n8henrie/Dropbox/Launch/n8log.log',
#    filemode='a'
    )
    
logger_name = str(__file__) + " :: " + str(__name__)
logger = logging.getLogger(logger_name)

logger.debug("Logging started.")

def internet_on():
    try:
        internet_on.internet_on()
        return True
    except:
        return False


def main():

    try:
        config = get_config.get_config()
    except Exception as e:
        print(e)
        print('Config file problem.')

    logger.debug("sys.argv length: {}".format(len(sys.argv)))

    if len(sys.argv) == 1:
        '''No arguments given with the script, so assume making a new task with note.'''
        now = datetime.datetime.now()
        ts = now.strftime('%Y%m%dT%H%M%S')

        task_name = '{}.txt'.format(ts)

        editor = config['EDITOR']['editor']
        task_folder = os.path.expanduser(config['DROPBOX']['task_folder'])
        task_path = os.path.join(task_folder, task_name)

        logger.debug("Calling editor {} to path {}".format(editor, task_path))

        subprocess.call([editor, task_path])

    elif len(sys.argv) > 1:
        '''Arguments given with script, so assume a one-liner and email using maildrop.'''

        task_list = sys.argv[1:]
        task = ' '.join(task_list)

        logger.debug("Passing to maildrop:\ntask: {}\nconfig:{}".format(task, config))
        maildrop.maildrop(task, config)

if __name__ == '__main__':
	main()