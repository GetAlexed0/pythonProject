import sys
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy

import twitter_credentials


class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)

        with open('tweets.json', 'a') as tf:
            tf.write(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == "__main__":

    listener = StdOutListener()
    auth = OAuthHandler(twitter_credentials.CONSUMER_KEY,
                        twitter_credentials.CONSUMER_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN,
                          twitter_credentials.ACCESS_TOKEN_SECRET)

    api = tweepy.(auth, listener)

    GEOBOX_GERMANY = [5.0770049095, 47.2982950435,
                      15.0403900146, 54.9039819757]

    stream.filter(locations=GEOBOX_GERMANY)
