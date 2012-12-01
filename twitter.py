import csv
import re

def ReadTweets(csvFileName):
    tweets = []

    with open(csvFileName, 'rb') as csvFile:
        reader = csv.reader(csvFile, delimiter=',', quotechar='"')
        for row in reader:
            # 3rd element in row (a list obj) is the tweet string
            tweets.append(Tweet(row[2]));

    return tweets



class Tweet(object):
    originalTweet  = ""
    parsedTweet    = ""
    tokens         = []
    incorrectWords = []
    hashtags       = []

    def __init__(self, originalTweet):
        self.originalTweet = originalTweet
        self.parsedTweet   = originalTweet
        self._parse()
        self._tokenize()

    def __str__(self):
        return self.originalTweet

    def _parse(self):
        # strip RT
        self.parsedTweet = re.sub(r"\bRT ", " ", self.parsedTweet)

        # lowercase
        self.parsedTweet = self.parsedTweet.lower()

        # strip url
        self.parsedTweet = re.sub(r"http(s?)\:\/\/([a-zA-Z0-9\/\.\-\_]*)", "", self.parsedTweet)

        # strip reply
        self.parsedTweet = re.sub(r"@(\w+)", "", self.parsedTweet)

        # strip hashtags
        self.hashtags    = re.findall(r"#(\w+)", self.parsedTweet)
        self.parsedTweet = re.sub(r"#(\w+)", "", self.parsedTweet)

        # strip non alphabet chars
        self.parsedTweet = re.sub(r"[^a-zA-Z\s]", " ", self.parsedTweet)

    def _tokenize(self):
        self.tokens = self.parsedTweet.split()