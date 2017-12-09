import urllib, json, praw
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
yesterday_url = "https://api.coindesk.com/v1/bpi/historical/close.json?for=yesterday"
valueOld = 1.000
value = 1.000
import praw

reddit = praw.Reddit(client_id='', client_secret='', user_agent='', username='', password='')
print(reddit.read_only)  # Output: False
submission = reddit.submission(url='https://www.reddit.com/r/test/comments/7ij0vc/bitbot/')
response = urllib.urlopen(url)
yesterday_response = urllib.urlopen(yesterday_url)
data = json.loads(response.read())
yesterday_data = json.loads(yesterday_response.read())
value = data["bpi"]["USD"]["rate_float"]
yesterday_value = yesterday_data["bpi"].itervalues().next() #Grab rate from previous day
cbv = 100 / value

while(True):
    valueOld = value
    response = urllib.urlopen(url)
    yesterday_response = urllib.urlopen(yesterday_url)
    data = json.loads(response.read())
    yesterday_data = json.loads(yesterday_response.read())
    value = data["bpi"]["USD"]["rate_float"]
    yesterday_value = yesterday_data["bpi"].itervalues().next()
    cbv = 100/value
    if valueOld != value:
        joke = "A boy asked his bitcoin investing dad for $100 worth of bitcoin currency. \nDad: $" + "{0:.2f}".format(valueOld * cbv) + "? What do you need $" + "{0:.2f}".format(value * cbv) + " for? Back in my day $" + "{0:.2f}".format(yesterday_value * cbv) + " could get you " + str(100/yesterday_value) + " of an entire bitcoin.\n     (live update to bitcoin value powered by coindesk)"
        submission.edit(joke)
        print joke
