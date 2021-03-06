
message = """
**Hey!**

The line "*%CITATION%*" is from **"%MOVIE%"**.

It begins at %START% and finishes at %END%.

Why do I do this? Not because we need but because we can.
___________________________
^(I am a small bot. Still need improving. Want to check out? Go to my source code and commit!)

[Source code](https://github.com/thecsw/sequelmemes_bot)
"""

summon_message = """
**Hello there!**

A lot of people do not know where the quotes come from and I am here to help you!

The line "*%CITATION%*" is from **"%MOVIE%"**.

I was summoned by %USERNAME%. If I am wrong, blame it on him! 
___________________________
^(I am a small bot. Still need improving. Want to check out? Go to my source code and commit!)

[Source code](https://github.com/thecsw/prequelmemes_bot)
"""

def modify_message(quote, movie, start, end):
    
    reply = message
    reply = reply.replace("%CITATION%", quote)
    reply = reply.replace("%START%", start)
    reply = reply.replace("%END%", end)
    reply = reply.replace("%MOVIE%", movie)

    return reply


def modify_summon_message(quote, movie, user):
    
    reply = summon_message
    reply = reply.replace("%CITATION%", quote)
    reply = reply.replace("%MOVIE%", movie)
    reply = reply.replace("%USERNAME%", user)
    
    return reply
