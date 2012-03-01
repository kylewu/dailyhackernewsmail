#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Wenbin Wu <wwu@mozilla.com>'
__date__ = '2012-03-01'

import smtplib
from email.mime.text import MIMEText

from jinja2 import Template

username = 'wenbin87@gmail.com'
password = 'sdbmypqiulsxjvrib'
fromaddr = 'wenbin87@gmail.com'
toaddr = 'wenbin87@gmail.com'


def send_mail(items):
    template = Template(open('mail.html').read())
    mail = template.render(items=items)

    mail = MIMEText(mail, 'html')
    mail['Subject'] = 'Daily Hakcer News'
    mail['From'] = fromaddr
    mail['To'] = toaddr

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddr, mail.as_string())
    server.quit()
