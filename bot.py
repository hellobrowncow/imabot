import tweepy

print('imabot')

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'
DIRECT_MESSAGE_FILE_NAME = 'last_seen_id.txt'
DIRECT_MESSAGE_LIMT=1000

def read_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def write_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def respond_to_mentioned_text():
    last_seen_id = read_last_seen_id(FILE_NAME)
    mentions = api.mentions.timeline(last_seen_id, tweet_mode='extended')
    for mention in reversed(mentions)
        print(mention.id + ' - ' + mention.full_text)
        last_seen_id = mention.id
        write_last_seen_id(last_seen_id, FILE_NAME)
        if '#FOUNDTEXT' in mention.text.lower():
            print('found #FOUNDTEXT')
            print('response ')
            api.update_status('@' + mention.user.screen_name + '#FOUNDTEXT! I like it!!', mention.id)

def read_direct_message(file_name):
    f_read = open(file_name, 'r')
    contents = f.read()
    f_read.close()
    return contents


def respond_to_direct_message();
    direct_messages = api.list_direct_messages(DIRECT_MESSAGE_LIMT)
    received_messages = direct_messages[0].received
    direct_message_text = read_direct_message(DIRECT_MESSAGE_FILE_NAME)
        for received_message in reversed(received_messages)
          api.send_direct_message(message[0].recipient_id, direct_message_text)

while True:
    respond_to_mentioned_text()
    time.sleep(300)