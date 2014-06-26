# smtplib module send mail

import smtplib
import configparser
import os.path
import get_config

def maildrop(task_name, task_note=None):
    try:
        config = get_config()
    except Exception as e:
        print('Config file problem.')

    maildrop_address = config['MAILDROP']['maildrop_address']
    SENDER = 'n8of.py'
    PORT = config['EMAIL']['port']
    SERVER_ADDRESS = config['EMAIL']['server_address']
    USER = config['EMAIL']['username']
    PASSWORD = config['EMAIL']['password']

    server = smtplib.SMTP(SERVER_ADDRESS, PORT)
    server.ehlo()
    server.starttls()
    server.login(USER, PASSWORD)

    MSG = (
            'To: {}'.format(maildrop_address)
            '\n'
            'From: {}'.format(SENDER)
            '\n'
            'Subject: {}'.format(task_name)
            '\n'
            task_note
            )

    server.sendmail(SENDER, [maildrop_address], MSG)
    server.quit()
