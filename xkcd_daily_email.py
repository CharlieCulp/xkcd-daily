#!/usr/bin/python3
# xkcd_daily_email.py
# Purpose: Email one xkcd comic daily in order, starting with 
# the last one I read. 

# This helped with getting days:
# https://dataquest.io/blog/python-datetime-tutorial/
# This helped with emailing, not encrypting password:
# https://dev.to/maxhumber/how-to-send-and-schedule-emails-with-python-dnb
# This helped with encrypting password:
# https://alexwlchan.net/2016/11/you-should-use-keyring/


from datetime import datetime, timedelta
from email.message import EmailMessage
import smtplib
import os
import keyring

# Get number for next comic's URL
last_read = 341    # Comic number in URL
now = datetime.now()
# print ("Today's date: ", str(now))

date_last_read = now - timedelta(days = last_read)
# print('date_last_read: ', date_last_read)

next_comic = (now - date_last_read).days    # .days converts it to an integer.
# print(next_comic)

SENDER = 'pydev714@gmail.com'
PASSWORD = keyring.get_password('email', 'pydev714@gmail.com')


def send_email(recipient, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = SENDER
    msg["To"] = recipient
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(SENDER, PASSWORD)
    server.send_message(msg)
    server.quit()


send_email("culpower@gmail.com", 
           subject="Daily xkcd",
           body="Here is the daily xkcd: http://xkcd.com/" + str(next_comic)
                   )


