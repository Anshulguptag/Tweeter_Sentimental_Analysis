from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import time
from senti_classifier import senti_classifier
import nltk
nltk.download('punkt')

consumer_key='AYDNqr9ycBI9qaOWoYXJgYnKY'
consumer_secret='tSHVPOr6JrQ9KNnqX1aSOGnKecmPeQQ37j81JAURI0t6deb8AA'

access_token='2493864625-SSCalZj2of8hITNgrv4gMvNZX7seGTSWD2MQI0H'
access_secret_token='5JBwqg2jWjijXgIRpEsdLrGRYWEuNmc4M0ibfRL2xzrhd'

class listener(StreamListener):
    def on_data(self,data):
        #file = open('C:/Users/anshul/jupyter/sample.txt', 'a')

        all_data=json.loads(data)
        tweet=all_data["text"]
        pos,neg =senti_classifier.polarity_scores(tweet)

        print(tweet)
        print(pos,neg)
        time.sleep(0.3)

        #file.write(': ' + str(d))
        #file.write('\n')
        #file.close()

        return True

    def on_error(self, status):
        print (status)


auth=OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret_token)
twitterStream=Stream(auth, listener())
twitterStream.filter(track=["Donald Trump"], locations=[-70.93044414,41.65536809,-70.9231071,41.66316909] )
