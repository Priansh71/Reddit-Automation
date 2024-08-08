import praw

reddit = praw.Reddit(user_agent="my_bot/0.1 by Automation-with-Python", client_id='xryg2RKcWH308ivq08PlsQ',
                     client_secret='p0dULNqYdWybnLOI4ARnHaz7eD2oHg',
                     username='Automation-with-Python',
                     password='QwertyQwerty123')

url = "https://www.reddit.com/r/IndianStockMarket/comments/1en37ya/what_do_youll_think_about_zerodha/"

post= reddit.submission(url=url)
print(post.title)
print(post.selftext)

print(len(post.comment)) # does not include nested comments
for comment in post.comment:
    print(comment.body)
