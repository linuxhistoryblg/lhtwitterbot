import tweepy
import os
from wmip import get_ip
from time import asctime

class Lhapp:
    def __init__(self, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET):
        self.CONSUMER_KEY = CONSUMER_KEY
        self.CONSUMER_SECRET = CONSUMER_SECRET
        self.ACCESS_KEY = ACCESS_KEY
        self.ACCESS_SECRET = ACCESS_SECRET
        # Auth with Twitter API (auth.set_access_token())
        self.auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        # Inst. API (twitter_API=tweepy.API(auth)
        self.auth.set_access_token(self.ACCESS_KEY, self.ACCESS_SECRET)
        # Authenticate : wait and message if rate limit exceeded
        self.twitter_API = tweepy.API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        # Test authentication
        try:
            self.twitter_API.verify_credentials()
            self.log_write('log.txt', 'Auth OK')
        except:
            self.log_write('log.txt', 'Unable to connect to twitter')

    def get_timestamp(self):
        return asctime()


    def log_write(self, log_file, log_message):
        self.logdir = os.path.dirname(os.path.realpath(__file__))
        with open(self.logdir + '/' + log_file, 'a') as f:
            f.write(f'{self.get_timestamp()} {log_message}\n')


    def get_dm_list(self):
        self.log_write('log.txt', 'GET latest DM')
        return self.twitter_API.list_direct_messages()


    def send_dm(self, recipient_id, text):
        # self.twitter_API.send_direct_message(recipient_id, text)
        self.twitter_API.send_direct_message(recipient_id, text)


    def destroy_dm(self, message_id):
        self.log_write('log.txt', f'{self.get_timestamp()} MSG DEL: {message_id}')
        self.twitter_API.destroy_direct_message(message_id)






