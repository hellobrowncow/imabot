import tweepy

print('imabot')

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def respond_to_mentioned_text():
    mentions = api.mentions.timeline()
    for mention in mentions
      print(mention.id + '-' + mention.text)
      if 'FOUNDTEXT' in mention.text.lower():
        print('found FOUNDTEXT')
        print('response ')

while True:
    respond_to_mentioned_text()
    time.sleep(300)