import json
from datetime import datetime

from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from SarcasmAnalysis import SarcasmAnalysis
import sys
sys.path.append("C:\Machine Learning\TwitterDemo\sarcasm-tweet-analysis/")


access_token = ''
access_token_secret = ''
consumer_key = ''
consumer_secret_key = ''


class TweetsStreamingListener(StreamListener):

    def __init__(self, time_limit=60):
        self.start_time = datetime.now()
        self.limit = time_limit
        self.tweet_data = []
        self.sarcasm_analysis = SarcasmAnalysis()

    def on_data(self, raw_data):
        try:
            self.tweet_data.append(raw_data)
            #print('raw data is =',raw_data)
            diff_time = (datetime.now() - self.start_time).seconds
            if diff_time == 1:
                print('started after ',diff_time ,' seconds and size of tweet array', len(self.tweet_data))
                tweets_list = []
                for tweet in self.tweet_data:
                    # now tweets will come in json format to convert into python we used loads method
                    tweet_json = json.loads(tweet)
                    tweets_list.append(tweet_json['text'])
                print(len(tweets_list))
                self.sarcasm_analysis.process_tweets(tweets_list)

                # we have appended data into tweet now when we execute this if statement
                # we need to should clear tweet_data array so that no variable should occupy space

                self.tweet_data = []
                print('finished processing sarcasm for tweets of size', len(tweets_list))
                return False
            return True
        except BaseException as e:
            print('Failed On data', str(e))

    def on_error(self, status_code):
        print(status_code)

    def on_timeout(self):
        print(sys.stderr, 'TimeOut....')


if __name__ == '__main__':
    print("inside main")
    authentication = OAuthHandler(consumer_key, consumer_secret_key)
    authentication.set_access_token(access_token, access_token_secret)
    stream = Stream(authentication, TweetsStreamingListener(time_limit=20))
    tweets = stream.filter(track='www.com')
