from dictionary import *   
    
yoloData = CalculateData("data/#YOLO_tweets_2012_11_29.csv", "swag")
swagData = CalculateData("data/#SWAG_tweets_2012_11_29.csv", "yolo")

print ""
print "#yolo"
print "n:",len(yoloData["tweets"])
print "sum:",yoloData["sumIncorrectWords"]
print "mean:",yoloData["meanIncorrectWords"]
print "std.dev:",yoloData["stdDeviation"]

print ""
print "#swag"
print "n:",len(swagData["tweets"])
print "sum:",swagData["sumIncorrectWords"]
print "mean:",swagData["meanIncorrectWords"]
print "std.dev:",swagData["stdDeviation"]