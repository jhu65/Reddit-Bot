import praw
import pdb
import os
import re

reddit = praw.Reddit(
    client_id='VXMpnVKBfEWHG0M0-yS4Mg',
    client_secret='QkPtuqyZeujS5TApWl6vuhnmBX0iPg',
    user_agent='<console:FirstApp:1.0>',
    username='ThrowawayMyFirstBot',
    password='MyBot657ForGood'
    )

subreddit = reddit.subreddit("pythonforengineers")
trigger = "MyWordCountBot!"

for submission in subreddit.new():
    for comment in submission.comments:
        if hasattr(comment, "body"):
            commentText = comment.body
            if trigger in commentText and commentText.index(trigger) == 0:
                search = commentText[len(trigger):]
                search = search.strip().lower()
                search = " " + search + " "
            
                redditor = comment.author
                count = 0
                for acctComments in redditor.comments.new(limit=None):
                    filteredComment = re.sub(r'[^\w\s]', '', acctComments)  # remove punctuation
                    count += filteredComment.lower().count(search)  # counts all the instances with spaces before and after
                
                comment.reply("Word count for:" + search + count +
                              "\n Counted by MyWordCountBot")