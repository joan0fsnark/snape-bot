
#!/usr/bin/python
import praw
import re
import random

snape_quotes = \
[
'The Dark Arts are many, varied, ever-changing, and eternal. Fighting them is like fighting a many-headed monster, which, each time a neck is severed, sprouts a head even fiercer and cleverer than before. You are fighting that which is unfixed, mutating, indestructible.',
'Tut, tut — fame clearly isn’t everything.',
'Well, it may have escaped your notice, but life isn’t fair.',
'The mind is not a book, to be opened at will and examined at leisure.',
'I don’t expect you will really understand the beauty of the softly simmering cauldron with its shimmering fumes, the delicate power of liquids that creep through human veins, bewitching the mind, ensnaring the senses...',
'You ought to be careful. People will think you’re… up to something.',
'Tell me, are you incapable of restraining yourself, or do you take pride in being an insufferable know-it-all?',
'Vengeance is very sweet.'
]

reddit = praw.Reddit(
        user_agent="SnapeBot (by u/USERNAME)",
        client_id=" ",
        client_secret=" ",
        username=" ",
        password=" ",
    )

subreddit = reddit.subreddit("pythonforengineers")

for comment in subreddit.stream.comments():
    print(comment.body)
    if re.search("always", comment.body, re.IGNORECASE):
            snape_reply = "Severus Snape says: " + random.choice(snape_quotes)
            comment.reply(snape_reply)
            print(snape_reply)