#! /usr/bin/env python3
'''n8of.py
A little module that will help me add tasks to OmniFocus from my other machines.

# Planned functionality:

- Will test for internet connectivity
- Given internet connectivity and a config, will email tasks to MailDrop
- Without internet connectivity, will add to a Dropbox folder, anticipating
the user will have Hazel and Dropbox add to OmniFocus
    '''

import sys

def main():

    if len(sys.argv) == 1:
        '''No arguments given with the script, so assume making a new task with note.'''

    elif len(sys.argv) > 1:
        '''Arguments given with script, so assume a one-liner and email using maildrop.'''

        task_list = sys.argv[1:]
        task = ' '.join(task_list)

