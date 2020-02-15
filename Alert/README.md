# Alert

A Reddit bot which listens for keywords in configured subreddit(s) new posts.
When a matching post is found it is sent to the configured email address.
This bot only listens for new posts after the time it is started. It does not
search existing posts on the subreddit.

## Configuration

Configure this bot by editing the `src/configuration.json` file. This JSON file is
structured as an object containing various fields that make up an alert. All fields (shown below) should be filled.

```
// configuration.json structure

{
  "name": "<alert-name>",
  "email": "<gmail-address>",
  "subreddits": [
    "<subreddit-1>",
    "<subreddit-2>",
           .
           .
           .
      "<subreddit-n>"
  ],
  "patterns": [
    "<pattern-1>",
    "<pattern-2>",
          .
          .
          .
    "<pattern-n>"
  ]
}
```

where each pattern is a regular expression. This implemetnation uses the Gmail API to insert emails into the inbox of the email address provided and so it must be a Gmail address. Note, no input validation is done on these fields.

### Setup Gmail

This bot uses the [Gmail API](https://developers.google.com/gmail/api/quickstart/python) to send emails. It will send emails to and from the address configured. Before using this bot you will need to setup Gmail authentication. 

1. Open [this site](https://developers.google.com/gmail/api/quickstart/python) in a browser and complete Step 1. Place the populated credentials.json file in this RedditBots/Alert/src`.
2. Run `quickstart.py` from within this directory and allow access to your Gmail account
3. (2) will create a token.pickle file within the RedditBots directory. This file is used for authentication.

### Multiple alerts

Unfortunately, PRAW's Reddit instance is [not thread safe](https://praw.readthedocs.io/en/latest/getting_started/multiple_instances.html#multiple-threads). As a result this bot cannot run multiple alerts at the same time. Each alert would need to run in a separate thread and access a single Reddit instance which is not safe.  

As mentioned in the docs multiple alerts will require multiple processes.