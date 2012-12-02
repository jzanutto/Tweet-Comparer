import csv
import re



def ReadTweets(csvFileName, excludeHash):
    tweets = []

    with open(csvFileName, 'rb') as csvFile:
        reader = csv.reader(csvFile, delimiter=',', quotechar='"')
        for row in reader:
            # 3rd element in row (a list obj) is the tweet string
            newTweet = Tweet(row[2])

            # only add tweet to output list if it doesn't contain the other hash tag that we are comparing
            if excludeHash not in newTweet.hashtags and len(newTweet.tokens) > 0:
                tweets.append(newTweet)

    return tweets



class Tweet(object):
    originalTweet  = ""
    parsedTweet    = ""
    tokens         = []
    hashtags       = set()
    incorrectWords = []

    def __init__(self, originalTweet):
        self.originalTweet = originalTweet
        self.parsedTweet   = originalTweet
        self._parse()
        self._tokenize()

    def __str__(self):
        return self.originalTweet

    def _parse(self):
        # strip HTML entities
        self.parsedTweet = re.sub(r"&(\w+);", " ", self.parsedTweet)

        # strip RT
        self.parsedTweet = re.sub(r"\bRT ", " ", self.parsedTweet)

        # lowercase
        self.parsedTweet = self.parsedTweet.lower()

        # strip url
        self.parsedTweet = re.sub(r"http(s?)\:\/\/([a-zA-Z0-9\/\.\-\_]*)", "", self.parsedTweet)

        # strip reply
        self.parsedTweet = re.sub(r"@(\w+)", "", self.parsedTweet)

        # create unique set of hashtags
        self.hashtags    = set(re.findall(r"#(\w+)", self.parsedTweet))
        
        # strip hashtags
        self.parsedTweet = re.sub(r"#(\w+)", "", self.parsedTweet)

        # strip contractions
        self.parsedTweet = re.sub(r"(\S?)(\w+)'(\w+)(\S?)", "", self.parsedTweet)

        # strip non alphabet chars
        self.parsedTweet = re.sub(r"[^a-zA-Z\s]", " ", self.parsedTweet)

        # strip all non 'i' or 'a' single char words
        self.parsedTweet = re.sub(r"\b(\s?)(^[ai])(\s?)\b", " ", self.parsedTweet)

    def _tokenize(self):
        self.tokens = self.parsedTweet.split()