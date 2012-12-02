from dictionary import *   


yoloData = CalculateData("data/#YOLO_tweets_2012_11_29.csv", "swag")
swagData = CalculateData("data/#SWAG_tweets_2012_11_29.csv", "yolo")



print ""
print "#yolo".rjust(9)
print "count:".rjust(10),   yoloData["count"]
print "sum:".rjust(10),     yoloData["sumIncorrectWords"]
print "mean:".rjust(10),    yoloData["meanIncorrectWords"]
print "std.dev:".rjust(10), yoloData["stdDeviation"]

open("output/yolo.correct", "w").close()
with open("output/yolo.correct", "a") as yoloCorrect:
    for word in yoloData["globalCorrectWords"]:
        yoloCorrect.write(word + "\n")

open("output/yolo.incorrect", "w").close()
with open("output/yolo.incorrect", "a") as yoloIncorrect:
    for word in yoloData["globalIncorrectWords"]:
        yoloIncorrect.write(word + "\n")

open("output/yolo.freq", "w").close()
with open("output/yolo.freq", "a") as yoloFreq:
    for mistakes in yoloData["globalFrequency"]:
        yoloFreq.write(str(mistakes).zfill(2) + " " + str(yoloData["globalFrequency"][mistakes]) + "\n")



print ""
print "#swag".rjust(9)
print "count:".rjust(10),   swagData["count"]
print "sum:".rjust(10),     swagData["sumIncorrectWords"]
print "mean:".rjust(10),    swagData["meanIncorrectWords"]
print "std.dev:".rjust(10), swagData["stdDeviation"]

open("output/swag.correct", "w").close()
with open("output/swag.correct", "a") as swagCorrect:
    for word in swagData["globalCorrectWords"]:
        swagCorrect.write(word + "\n")

open("output/swag.incorrect", "w").close()
with open("output/swag.incorrect", "a") as swagIncorrect:
    for word in swagData["globalIncorrectWords"]:
        swagIncorrect.write(word + "\n")

open("output/swag.freq", "w").close()
with open("output/swag.freq", "a") as swagFreq:
    for mistakes in swagData["globalFrequency"]:
        swagFreq.write(str(mistakes).zfill(2) + " " + str(swagData["globalFrequency"][mistakes]) + "\n")