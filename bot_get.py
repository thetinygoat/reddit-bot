import praw
import pdb
import re
import os


if not os.path.isfile("replied_to.txt"):
    replied_to = []
else:
    with open("replied_to.txt", "r") as f:
        replied_to = f.read()
        replied_to = replied_to.split("\n")
        replied_to = list(filter(None,replied_to));
reddit = praw.Reddit('pybot')
subreddit = reddit.subreddit('pythonforengineers')

for submission in subreddit.hot(limit=10):
    if submission.id not in replied_to:
        if re.search("i love python", submission.title, re.IGNORECASE):
            submission.reply("beep boop this is a test reply i am a bot!")
            print("bot replying to : ", submission.title)
            replied_to.append(submission.id)
with open("replied_to.txt", "w") as f:
    for post_id in replied_to:
        f.write(post_id + "\n")