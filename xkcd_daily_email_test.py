#!/usr/bin/python3
# xkcd_daily_email.py
# Purpose: Email one xkcd comic daily and in order. 

# This helped with getting days sorted out:
# -> https://dataquest.io/blog/python-datetime-tutorial/
# This helped with emailing, NOT encrypting password:
# -> https://dev.to/maxhumber/how-to-send-and-schedule-emails-with-python-dnb
# This helped with encrypting password:
# -> https://alexwlchan.net/2016/11/you-should-use-keyring/


from datetime import datetime, timedelta
from email.message import EmailMessage
import smtplib
import os
import keyring

# Get number for next comic's URL
anchor_date = datetime(2020, 1, 14)    # The date that matches the last comic read in "days ago"
now = datetime.now()
print("Anchor date: " + str(anchor_date))
print ("Today's date: ", str(now))
next_comic = (now - anchor_date).days     # .days converts it to an integer.
print(str(next_comic))

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


# send_email("culpower@gmail.com", 
#            subject="Daily xkcd",
#            body="Here is the daily xkcd: http://xkcd.com/" + str(next_comic)
#                    )


