import json

# open the JSON file
tweetFile = open("tweets.json", "r")

# get the data
tweetData = json.load(tweetFile)

# close the file
tweetFile.close()

# print location of the first tweet's author
print(tweetData[0]["user"]["location"])

# print text for the first tweet
print(tweetData[0]["text"])

# one way to print all the tweet text in our file
# this way allows us to access the position of the tweet within the list
for tweetNum in range(len(tweetData)):
    print(tweetData[tweetNum]["text"])

# a second way to print all the tweet text in our file
# this one doesn't allow us to match list numbers to tweets, but it is more succint
for tweet in tweetData:
    print(tweet["text"])
