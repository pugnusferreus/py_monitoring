#!/usr/bin/python

import httplib
import smtplib
from email.mime.text import MIMEText

EMAIL_LIST = ['your@email.com']
COMMASPACE = ', '

def get_status_code(host, path="/"):
    try:
        conn = httplib.HTTPConnection(host)
        conn.request("HEAD", path)
        return conn.getresponse().status
    except StandardError:
        return None

def send_email(receivers, subject, message):
	SERVER = "your_smtp_server"
	FROM = "your_monitoring@email.com"

	# Prepare actual message

	mimeText = MIMEText(message)
	mimeText['From'] = FROM
	mimeText['To'] = COMMASPACE.join(receivers)
	mimeText['Subject'] = subject

	# Send the mail

	server = smtplib.SMTP(SERVER)
	server.sendmail(FROM, receivers, mimeText.as_string())
	server.quit()


if get_status_code("127.0.0.1","/index.html") != 200:
	send_email(EMAIL_LIST ,'Localhost not responding', 'Hey! Localhost not responding')
