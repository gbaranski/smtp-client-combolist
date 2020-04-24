import json
SMTPserver = 'SMTPSERVER'
destination = ['test@gmail.com']

# typical values for text_subtype are plain, html, xml
text_subtype = 'plain'

content="""\
Test message
"""

subject="Sent from Python"

import sys
import os
import re
import smtplib as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
import socket

# from smtplib import SMTP                  # use this for standard SMTP protocol   (port 25, no encryption)

# old version
# from email.MIMEText import MIMEText
from email.mime.text import MIMEText

with open('input/authme.json') as json_file:
    jsondata = json.load(json_file)
    for data in jsondata:
        if(data['email']):
            if ("@DOMAINNAME" in data['email']):     
                USERNAME = data['email']
                PASSWORD = data['password']
                sender = USERNAME
                try:
                    print(USERNAME + ":" + PASSWORD)
                    msg = MIMEText(content, text_subtype)
                    msg['Subject']=       subject
                    msg['From']   = sender # some SMTP servers will do this automatically, not all
                    conn = SMTP.SMTP(SMTPserver)
                    #conn = SMTP(SMTPserver)
                    conn.set_debuglevel(False)
                    conn.login(USERNAME, PASSWORD)
                    try:
                        conn.sendmail(sender, destination, msg.as_string())
                    finally:
                        print("WORKING")
                        conn.quit()
                except socket.error as e:
                    print(e)
                    # sys.exit( "mail failed; %s" % "CUSTOM_ERROR" ) # give an error message
