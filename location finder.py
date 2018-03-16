import time
import tweepy

consumer_key='AYDNqr9ycBI9qaOWoYXJgYnKY'
consumer_secret='tSHVPOr6JrQ9KNnqX1aSOGnKecmPeQQ37j81JAURI0t6deb8AA'

access_token='2493864625-SSCalZj2of8hITNgrv4gMvNZX7seGTSWD2MQI0H'
access_secret_token='5JBwqg2jWjijXgIRpEsdLrGRYWEuNmc4M0ibfRL2xzrhd'
string_to_search = 'WWE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret_token)

api = tweepy.API(auth)

past_status_ids = set()

while True:
    tweets = api.search(q=string_to_search)
tweet_id_list = set([tweet.id for tweet in tweets])
new_tweet_ids = tweet_id_list - past_status_ids
past_status_ids = tweet_id_list | past_status_ids



for tweet_id in new_tweet_ids:
    print ("Retweeting " + str(tweet_id))
    api.retweet(tweet_id)
    #username = tweets.user.screen_name
    #api.create_friendship(username)
    #print "Followed " + str(username)
    limits = api.rate_limit_status()
    remain_search_limits = limits['resources']['search']['/search/tweets']['remaining']
    print("Limit left is " + str(remain_search_limits))
    print("")
    time.sleep(150)