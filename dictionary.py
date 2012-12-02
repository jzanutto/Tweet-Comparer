from twitter import *
from math import sqrt, pow



def BuildDictionary():
    dictionary = set()
    wordList   = open("data/dict-v2.txt", "r")
    validWords = set()

    for word in wordList:
        dictionary.add(word.strip().lower())

<<<<<<< HEAD
    return dictionary
=======
dictionary = set(validWords)
>>>>>>> 216a34a93e4d5b0416ead50786890cc95e67f2ae



def CalculateData(tweetsFile, excludeHash):
    dictionary           = BuildDictionary()
    tweets               = ReadTweets(tweetsFile, excludeHash)
    globalCorrectWords   = set()
    globalIncorrectWords = set()
    globalFrequency      = dict()
    
    sumIncorrectWords  = 0
    meanIncorrectWords = 0.0
    
    sumMeanDifference = 0.0
    stdDeviation      = 0.0

    # setup global histogram
    for x in xrange(0, 31):
        globalFrequency[x] = 0;

    # process tweets
    for tweet in tweets:
        currentIncorrectWords = [] # a list because a user can misspell the same word multiple times
        for token in tweet.tokens:

            mistakes    = 0;
            grammarList = [token]

            if len(token) > 3 and token[-1] == "s":
                grammarList.append(token[:-1])
            if len(token) > 3 and token[-2:] == "ed":
                grammarList.append(token[:-2])
                grammarList.append(token[:-2] + "e")
            if len(token) > 5 and token[-3:] == "ing":
                grammarList.append(token[:-3])
                grammarList.append(token[:-3] + "e")
            if len(token) > 5 and token[-3:] == "ies":
                grammarList.append(token[:-3] + "y")

            for variation in grammarList:
                if variation not in dictionary:
                    mistakes += 1

            # we are 100% sure that the token is incorrect if ALL of its possible derivations are
            # not in the dictionary
            if mistakes == len(grammarList):
                # only add to this tweet's incorrect words if not alread added
                currentIncorrectWords.append(token)
                # add to global list of incorrect words
                globalIncorrectWords.add(token)
            else :
                globalCorrectWords.add(token)

        tweet.incorrectWords = currentIncorrectWords
        sumIncorrectWords   += len(tweet.incorrectWords)

        # increment histogram
        globalFrequency[len(tweet.incorrectWords)] += 1 

    # calculate mean and std dev
    meanIncorrectWords = float(sumIncorrectWords) / len(tweets)
    for tweet in tweets:
        sumMeanDifference += pow(len(tweet.incorrectWords) - meanIncorrectWords, 2)
    stdDeviation = sqrt(sumMeanDifference / (len(tweets) - 1))

    return dict(
                    count                = len(tweets),
                    sumIncorrectWords    = sumIncorrectWords,
                    meanIncorrectWords   = meanIncorrectWords,
                    stdDeviation         = stdDeviation,
                    globalCorrectWords   = globalCorrectWords,
                    globalIncorrectWords = globalIncorrectWords,
                    globalFrequency      = globalFrequency
                )
