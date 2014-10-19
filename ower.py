#! /usr/bin/python
# Udacity final Project
# This class is part of a app called owee

import smtplib
import re
import getpass
import socket
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Ower():
    """This class define all the attributes of the person borrowing the item"""
    def __init__(self, ower_first_name, ower_last_name, ower_email,
                 ower_phone, ower_address):
        self.first_name = ower_first_name
        self.last_name = ower_last_name
        self.email = ower_email
        self.phone = ower_phone
        self.address = ower_address

    def send_reminder(self):
        """send a message to the ower reminding him about his loan"""
        print ('Send a reminder')
        sender = str(raw_input('Enter your email (only Gmail or Yahoo '
                               'are valid for now): ')).lower().strip()
        sender_password = getpass.getpass('Enter your '
                                          'email password: ').strip()
        hostname = ''
        webmail = ''
        while True:
            match = re.match(r'\w+@(\w+)\.\D+', sender)
            try:
                webmail = match.group(1)
                if webmail == 'yahoo':
                    hostname = 'smtp.mail.yahoo.com'
                    break

                elif webmail == 'gmail':
                    hostname = 'smtp.gmail.com'
                    break
                else:
                    print ('This email provider is not used by this '
                           'application yet use Gmail or Yahoo Mail')
                    sender = str(raw_input('Enter your '
                                           'email: ')).lower().strip()
                    sender_password = getpass.getpass('Enter your email password: ').strip()
            except:
                sender = raw_input('Invalid mail, retry: ')
                sender_password = getpass.getpass('Enter your email password: ')
        # Connection to server and message sending
        try:
            smtpserver = smtplib.SMTP(hostname, 587)
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo()
            print '\nConnection to {0:s} successful \n'.format(webmail.capitalize())
            while True:
                # try to connect to the server
                try:
                    smtpserver.login(sender, sender_password)
                    break
                # if user connection to webmail failed handle the exception
                except smtplib.SMTPException:
                    print ('Authentication failed, wrong password or mail combo.' + '\n')
                    sender = str(raw_input('Enter email: ')).lower().strip()
                    sender_password = getpass.getpass('Enter your '
                                                      'email password: ').strip()
        # handle the exception if connection to webmail host failed
        except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException), e:
            print ('Connection to {0:s} failed'.format(webmail) + '\n')
            print e
            print hostname
            getpass.getpass('Press enter to leave.')
            sys.exit(1)

        # format the message to be sent
        to = self.email
        msg = MIMEMultipart('alternative')
        msg['Subject'] = str(raw_input('Subject: ')).strip()
        msg['From'] = sender
        msg['To'] = to

        # create the body of the message
        message_body = str(raw_input('Message: '))
        html = """
        <html>
            <head></head>
            <body>
                {body}
            </body>
        </html>
        """
        html = html.format(body=message_body)
        message = MIMEText(html, 'html')
        msg.attach(message)
        # try to send message
        try:
            smtpserver.sendmail(sender, to, msg.as_string())
        except smtplib.SMTPException:
            print ('Email could not be sent, retry please.')
            smtpserver.close()
            getpass.getpass('Press enter to leave')
            sys.exit(1)

        print ('\nEmail Sent Successfully \n')
