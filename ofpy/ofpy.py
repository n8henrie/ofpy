#! /usr/bin/env python3
'''n8of.py
A little module that will help me add tasks to OmniFocus from my other non-Mac machines.

# Planned functionality:

- Will test for internet connectivity
- Given internet connectivity and a config, will email tasks to MailDrop
- Without internet connectivity, will add to a Dropbox folder, anticipating
the user will have Hazel and Dropbox add to OmniFocus
    '''

import sys
import internet_on
import get_config
import datetime # todo: datetime timestamp setup
import logging # todo: logging setup
import os.path
import maildrop

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

    if len(sys.argv) == 1:
        '''No arguments given with the script, so assume making a new task with note.'''
        ts = datetime.datetime.now()
        task_name = '{}.txt'.format(ts)

        editor = config['EDITOR']['editor']
        task_folder = config['DROPBOX']['task_folder']
        task_path = os.path.join([task_folder, task_name])

        subprocess.call([editor, task_path])

    elif len(sys.argv) > 1:
        '''Arguments given with script, so assume a one-liner and email using maildrop.'''

        task_list = sys.argv[1:]
        task = ' '.join(task_list)

        maildrop.maildrop(task, config)

