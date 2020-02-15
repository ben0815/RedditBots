#!/usr/local/bin/python3

import base64
import os
import pickle
import praw
import json
import re
import smtplib
import sys

from apiclient import errors

from email.mime.text import MIMEText

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# Initialize reddit object with .ini file.
reddit = praw.Reddit('Alert')

def main():
    print("Successfully logged into Reddit with username ", reddit.user.me(),
            ".", sep = '')

    with open(os.path.join(sys.path[0], 'configuration.json')) as configuration_file:
        configuration = json.load(configuration_file)

    service = setup_gmail()

    # For some reason reddit.multireddit does not work for me.
    multireddit = '+'.join(configuration["subreddits"])

    print(multireddit)

    re_objects = [re.compile(pattern) for pattern in configuration["patterns"]]
    for submission in reddit.subreddit(multireddit).stream.submissions(skip_existing=True):
        for reo in re_objects:
            if re.search(reo, submission.title + submission.selftext) is not None:
                send_email(service, configuration["email"], create_message(configuration["email"], 'Alert - ' + configuration["name"], submission.shortlink))

def setup_gmail():
    creds = None

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                os.path.join(sys.path[0], 'credentials.json'), SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('gmail', 'v1', credentials=creds)

def create_message(address, subject, body):
    message = MIMEText(body)
    message['to'] = address
    message['from'] = address
    message['subject'] = subject 
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

def send_email(service, address, message):
    try:
        print('Sending email: ', message)
        service.users().messages().send(userId=address, body=message).execute()
    except errors.HttpError as error:
        print('An error occurred: ', error)

if __name__ == '__main__':
    main()
