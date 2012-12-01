from twitter import *
from dictionary import *

dictionary = BuildDictionary("data/dict-v2.txt")
yoloTweets = ReadTweets("data/#YOLO_tweets_2012_11_29.csv")
swagTweets = ReadTweets("data/#SWAG_tweets_2012_11_29.csv")





for tweet in yoloTweets:
    print "---------------------------"
    print ""
    print tweet.originalTweet
    print tweet.parsedTweet
    print ""

    for word in tweet.tokens:
        print word
    
    print ""