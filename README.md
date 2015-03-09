# py_monitoring

A simple Python script to allow you to monitor your webservers.

1. Make sure that you have a Python 2.x interpreter on your machine. I've not tried this script with Python 3.
2. Open monitoring.py with your favourite text editor.
3. Change the `EMAIL_LIST` variable, `SERVER` and `FROM` variable.
4. On line 36 and 37, change your webserver address and the email subject and message.
5. Add this script to your crontab. For example, to run every 5 minutes, type `crontab -e` and enter `*/5 * * * * /home/<your home>/monitor.py`
