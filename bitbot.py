import urllib, json, praw
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
valueOld = 1.000
value = 1.000
import praw

reddit = praw.Reddit(client_id='', client_secret='', user_agent='', username='', password='')
print(reddit.read_only)  # Output: False
submission = reddit.submission(url='https://www.reddit.com/r/test/comments/7ij0vc/bitbot/')
response = urllib.urlopen(url)    
data = json.loads(response.read())
value = data["bpi"]["USD"]["rate_float"]
cbv = 100 / value 

while(True):
    valueOld = value
    response = urllib.urlopen(url)    
    data = json.loads(response.read())
    value = data["bpi"]["USD"]["rate_float"]
    if valueOld != value:
        joke = "A boy asked his bitcoin investing dad for 100. \nDad: $" + "{0:.2f}".format(valueOld * cbv) + "? What do you need $" + "{0:.2f}".format(value * cbv) + " for?\n     (live update to bitcoin value powered by coindesk)"
        submission.edit(joke)
        print joke
