# Alert

A Reddit bot which listens for keywords in configured subreddit(s) new posts.
When a matching post is found it is sent to the configured email address.
This bot only listens for new posts after the time it is started. It does not
search existing posts on the subreddit.

## Configuration

Configure this bot by editing the `src/configuration.json` file. This JSON file is
structured as an object containing alerts as name, object pairs.

```
// configuration.json structure

{
  "<alert-name>": {
    "email": "<email-address>",
    "subreddits": [
      "<subreddit-1>",
      "<subreddit-2>",
             .
             .
             .
      "<subreddit-n>",
    ],
    "keywords": [
      "<keyword-1>",
      "<keyword-2>",
            .
            .
            .
      "<keyword-n>",
    ]
  },
  ... // more alerts
}
```

### Keywords

TODO: Write about what type of keywords can be used.
