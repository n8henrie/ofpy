"""maildrop.py
Helps ofpy send tasks to OmniFocus by using the OmniGroup MailDrop
service. See http://support.omnigroup.com/omnifocus-mail-drop
"""

import smtplib
import os.path
from email.mime.text import MIMEText
import logging
import datetime
import platform

logging.basicConfig(
    level=logging.WARNING,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
    )

logger_name = str(__file__) + " :: " + str(__name__)
logger = logging.getLogger(logger_name)


def maildrop(task, config, task_note=None):

    if not task_note:
        now = datetime.datetime.now()
        now_str = datetime.datetime.isoformat(now)

        try:
            host = platform.node()
        except:
            host = 'undetermined'

        task_note = "Sent on {} from {}".format(now_str, host)

    maildrop_address = config.get('MAILDROP', 'maildrop_address')
    SENDER = 'ofpy.py'
    PORT = config.get('EMAIL', 'port')
    SERVER_ADDRESS = config.get('EMAIL', 'server_address')
    USER = config.get('EMAIL', 'username')
    PASSWORD = config.get('EMAIL', 'password')

    logger.debug("Attempting to login in with credentials:\n"
                 "user: {}\n"
                 "pass: {}\n"
                 "server address: {}\n".format(USER, PASSWORD,
                                               SERVER_ADDRESS))

    server = smtplib.SMTP(SERVER_ADDRESS, PORT)
    server.ehlo()
    server.starttls()

    try:
        server.login(USER, PASSWORD)
    except smtplib.SMTPAuthenticationError as e:
        logger.exception("Smtplib didn't like your login credentials. Please"
                         " double check your ~/.ofpy_config .")

    logger.debug("Task details:\n"
                 "task: {}\n"
                 "task note: {}".format(task, task_note))

    msg = MIMEText(task_note)
    msg['To'] = maildrop_address
    msg['From'] = SENDER
    msg['Subject'] = task

    server.send_message(msg)
    server.quit()
