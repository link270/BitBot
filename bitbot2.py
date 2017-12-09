import urllib, json, praw
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
valueOld = 1.000
value = 1.000
import praw

reddit = praw.Reddit(client_id='probably should hide this', client_secret='like it says secret', user_agent='BitBot: by /u/theFlyingFirstAidKit', username='theFlyingFirstAidKit', password='Im not puting my password here online')
print(reddit.read_only)  # Output: False
submission = reddit.submission(url='https://www.reddit.com/r/test/comments/7ij0vc/bitbot/')

while(True):
    valueOld = value
    response = urllib.urlopen(url)    
    data = json.loads(response.read())
    value = data["bpi"]["USD"]["rate_float"]
    if valueOld != value:
        joke = "A boy asked his bitcoin investng dad for .1 Bitcoin. \nDad: $" + "{0:.2f}".format(valueOld / 10) + "? What do you need $" + "{0:.2f}".format(value / 10) + " for?\n     (live update to bitcoin value powered by coindesk)"
        submission.edit(joke)
        print joke
