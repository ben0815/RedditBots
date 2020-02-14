#!/usr/local/bin/python3

import praw
import json


# Initialize reddit object with .ini file.
reddit = praw.Reddit('Authentication')

def main():
    print("Successfully logged into Reddit with username ", reddit.user.me(),
            ".", sep = '')

    with open('configuration.json') as configuration_file:
        configuration = json.load(configuration_file)

    alert = configuration["test-alert"]
    email = alert["email"]
    subbreddits = alert["subreddits"]
    keywords = alert["keywords"]

    print(email)
    print(subreddits)
    print(keywords)

    # Create multireddit of subreddits
    # stream new submissions
    # Search for keywords

    # Continuously search for phrases in comments of given subreddit(s).
    while(True):
        pass

if __name__ == '__main__':
    main()
