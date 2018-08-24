'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("tweets.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

vispolarity = []
vissubjectivity = []

for tweetNum in range(len(tweetData)):
    tb = TextBlob(tweetData[tweetNum]["text"])
    vispolarity.extend([tb.polarity])

# a second way to print all the tweet text in our file
# this one doesn't allow us to match list numbers to tweets, but it is more succint
for tweet in tweetData:
    tb = TextBlob(tweet["text"])
    vissubjectivity.extend([tb.subjectivity])

def average_polarity(vispolarity):
    return sum(vispolarity) / len(vispolarity)
def average_subjectivity(vissubjectivity):
    return sum(vissubjectivity) / len(vissubjectivity)

x = average_polarity(vispolarity)
print("This is the polarity: " + str(x))
y = average_subjectivity(vissubjectivity)
print("This is the Subjectivity: " + str(y))
def all_graphs():
    plt.hist(vispolarity)
    plt.title("Polarity")
    plt.xlabel("Polarity")
    plt.ylabel("Number of Tweets")
    plt.show()

    plt.hist(vissubjectivity)
    plt.title("Subjectivity")
    plt.xlabel("Subjectivity")
    plt.ylabel("Number of Tweets")
    plt.show()

    a = vissubjectivity
    b = vispolarity
    plt.scatter(a,b)
    plt.title("Polarity vs. Subjectivity")
    plt.xlabel("Subjectivity")
    plt.ylabel("Polarity")
    plt.show()
all_graphs()

name = [-2, -1, 0, 1, 2]
value = [1, 10, 100]
plt.figure(1, figsize=(50,20))
plt.subplot(131)
plt.hist(value, name)
plt.suptitle('Categorical Plotting')
plt.show()
