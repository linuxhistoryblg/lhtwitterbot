import tweepy

# Twitter Creds
CONSUMER_KEY = '<Your consumer key>'
CONSUMER_SECRET = '<Your consumer secret>'
ACCESS_KEY = '<Your access key>'
ACCESS_SECRET = '<Your access secret>'

def get_dm_list():
    return twitter_API.list_direct_messages()


# Auth with Twitter API (auth.set_access_token())
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# Inst. API (twitter_API=tweepy.API(auth)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
# Authenticate : wait and message if rate limit exceeded
twitter_API = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
# Test authentication
try:
    twitter_API.verify_credentials()
    print('AUTH OK')
except:
    print('Unable to connect to twitter')

# Get DM List
dm_list = get_dm_list()

# Check queue length, exit if no messages
if len(dm_list) == 0:
    print('Error: No messages in queue.')
    exit(1)

# Extract relevant fields
message = dm_list[0]._json
message_id = message['id']
sender_id = message['message_create']['sender_id']
message_text = message['message_create']['message_data']['text']

print(f'If your message was {message_text} your sender id is {sender_id}')
