from twitter import *
from math import pow, sqrt



dictionary = []
wordList   = open("data/dict-v2.txt", "r")
validWords = set()

for word in wordList:
    validWords.add(word.lower())

dictionary = list(validWords)



def CalculateData(tweetsFile, excludeHash):
    tweets               = ReadTweets(tweetsFile, excludeHash)
    globalIncorrectWords = dict()
    
    sumIncorrectWords  = 0
    meanIncorrectWords = 0.0
    
    sumMeanDifference = 0.0
    stdDeviation      = 0.0

    for tweet in tweets:
        currentIncorrectWords = set()

        for token in tweet.tokens:
            if token not in dictionary:
                # only add to this tweet's incorrect words if not alread added
                if token not in currentIncorrectWords:
                    currentIncorrectWords.add(token)

                # add to global list of incorrect words
                # for histogram later
                if token not in globalIncorrectWords:
                    globalIncorrectWords[token] = 1
                else :
                    globalIncorrectWords[token] = globalIncorrectWords.get(token) + 1

        tweet.incorrectWords = list(currentIncorrectWords)
        sumIncorrectWords   += len(tweet.incorrectWords)

    meanIncorrectWords = sumIncorrectWords / len(tweets)

    for tweet in tweets:
        sumMeanDifference += pow(len(tweet.incorrectWords) - meanIncorrectWords, 2)

    stdDeviation = sqrt(sumMeanDifference / (len(tweets) - 1))

    return dict(
                    tweets               = tweets,
                    sumIncorrectWords    = sumIncorrectWords,
                    meanIncorrectWords   = meanIncorrectWords,
                    stdDeviation         = stdDeviation,
                    globalIncorrectWords = globalIncorrectWords
                )
