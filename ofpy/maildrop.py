# smtplib module send mail

import smtplib
import os.path
from email.mime.text import MIMEText

def maildrop(task_note=None, task, config):

    maildrop_address = config['MAILDROP']['maildrop_address']
    SENDER = 'ofpy.py'
    PORT = config['EMAIL']['port']
    SERVER_ADDRESS = config['EMAIL']['server_address']
    USER = config['EMAIL']['username']
    PASSWORD = config['EMAIL']['password']

    server = smtplib.SMTP(SERVER_ADDRESS, PORT)
    server.ehlo()
    server.starttls()
    server.login(USER, PASSWORD)

    msg = MIMEText(task_note)
    msg['Subject'] = task
    msg['From'] = SENDER
    msg['To'] = maildrop_address

    server.sendmail(SENDER, [maildrop_address], MSG)
    server.quit()
