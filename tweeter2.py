import tweepy
import numpy as np
import pandas as pd
import datetime
import re
from datetime import date, timedelta
####input your credentials here
consumer_key = 'AYDNqr9ycBI9qaOWoYXJgYnKY'
consumer_secret = 'tSHVPOr6JrQ9KNnqX1aSOGnKecmPeQQ37j81JAURI0t6deb8AA'
access_token = '2493864625-SSCalZj2of8hITNgrv4gMvNZX7seGTSWD2MQI0H'
access_token_secret = '5JBwqg2jWjijXgIRpEsdLrGRYWEuNmc4M0ibfRL2xzrhd'
f = open('C:/Users/anshul/jupyter/sample.txt', 'r+')
f.truncate()
hashtagtweet=input("Enter the hash tag tweet: ")
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
df=pd.read_csv('positive.txt', header=None)
positive_vocab=np.concatenate(np.array(df), axis=0)
now=datetime.datetime.now()
enddate=now.date()
startdate=enddate - timedelta(10)
df1=pd.read_csv('negative.txt', header=None)
print (startdate, enddate)
negative_vocab=np.concatenate(np.array(df1), axis=0)
for tweet in tweepy.Cursor(api.search,q=hashtagtweet,count=100,
                           lang="en",
                           since=startdate, until=enddate).items():
    file = open('C:/Users/anshul/jupyter/sample.txt', 'a')
    #pos, neg=senti_classifier.polarity_scores(tweet.text)
    print (tweet.created_at, tweet.text)
    pos=0
    neg=0
    sentence = tweet.text
    '''
    if ':' in sentence:
        sentence = (sentence.rsplit(':')[1]).rsplit('.', 1)[0]
    else:
        sentence = sentence.rsplit('.', 1)[0]
    '''
    #sentence = sentence.replace('RT @', '')
    sentence = re.sub('[^ a-zA-Z0-9' ']', '', sentence)
    file.write('Tweet: '+str(tweet.created_at)+' : ' + str(sentence))

    sentence = sentence.lower()
    words = (sentence).split(' ')
    for word in words:
        #print (word)
        if word in positive_vocab:
            pos+=1
        elif word in negative_vocab:
            neg+=1


    if pos>neg:
        d='Positive'
    elif pos<neg:
        d='Negative'
    else:
        d='Neutral'
    file.write(': ' + str(d))
    file.write('\n')
    print (d)
    #time.sleep(1)
    file.close()

