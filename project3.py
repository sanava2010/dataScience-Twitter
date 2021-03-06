# Import libraries
import tweepy # Twitter
import numpy
import pandas
import matplotlib
from textblob import TextBlob, Word # Text pre-processing
import re # Regular expressions
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator # Word clouds
from PIL import Image
from pyspark.sql import SparkSession # Spark

# Import Twitter authentication file
from twitter_auth import *

# Twitter authentication
def twitter_auth():
    # This function has been completed for you
    # It uses hardcoded Twitter credentials and returns a request handler
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    return tweepy.API(auth)

# Retrieve Tweets
def get_tweets():
    # This function has been completed for you
    # It creates a Tweet list and extracts Tweets
    account = 'CNN' # You can change this to any Twitter account you wish
    extractor = twitter_auth() # Twitter handler object
    tweets = []
    for tweet in tweepy.Cursor(extractor.user_timeline, id = account).items():
        tweets.append(tweet)
    print('Number of Tweets extracted: {}.\n'.format(len(tweets)))
    return tweets

# Create dataframe
def make_dataframe(tweets):
    # This function should return a dataframe containing the text in the Tweets
    return pandas.DataFrame(data = ..., columns = ['Tweets'])

# Pre-process Tweets
def clean_tweets(data):
    # This function has been completed for you
    # It pre-processes the text in the Tweets and runs in parallel
    spark = SparkSession\
    .builder\
    .appName("PythonPi")\
    .getOrCreate()
    sc = spark.sparkContext
    paralleled = sc.parallelize(data)
    return paralleled.map(text_preprocess).collect()

# Pre-process text in Tweet
def text_preprocess(tweet):
    # This function should return a Tweet that consists of only lowercase characters,
    # no hyperlinks or symbols, and has been stemmed or lemmatized
    # Hint: use TextBlob and Word(tweet) and look up which functions you can call
    tweet = ...
    ...
    return tweet

# Retrieve sentiment of Tweets
def generate_sentiment(data):
    # This function has been completed for you
    # It returns the sentiment of the Tweets and runs in parallel
    spark = SparkSession\
    .builder\
    .appName("PythonPi")\
    .getOrCreate()
    sc = spark.sparkContext
    paralleled = sc.parallelize(data)
    return paralleled.map(data_sentiment).collect()

# Retrieve sentiment of Tweet
def data_sentiment(tweet):
    # This function should return 1, 0, or -1 depending on the value of text.sentiment.polarity
    text = TextBlob(...)
    if ...:
        return 1
    elif ...:
        return 0
    else:
        return -1

# Classify Tweets
def classify_tweets(data):
    # Given the cleaned Tweets and their sentiment,
    # this function should return a list of good, neutral, and bad Tweets
    good_tweets = ""
    neutral_tweets = ""
    bad_tweets = ""
    ...
    return [good_tweets, neutral_tweets, bad_tweets]

# Create word cloud
def create_word_cloud(classified_tweets) :
    # Given the list of good, neutral, and bad Tweets,
    # create a word cloud for each list
    # Use different colors for each word cloud
    good_tweets = ...
    neutral_tweets = ...
    bad_tweets = ...
    stopwords = set(STOPWORDS)
    good_cloud = WordCloud(...)
    neutral_cloud = WordCloud(...)
    bad_cloud = WordCloud(...)
    ...
    produce_plot(good_cloud, "Good.png")
    produce_plot(neutral_cloud, "Neutral.png")
    produce_plot(bad_cloud, "Bad.png")

# Produce plot
def produce_plot(cloud, name):
    # This function has been completed for you
    matplotlib.pyplot.axis("off")
    matplotlib.pyplot.imshow(cloud, interpolation='bilinear')
    fig = matplotlib.pyplot.figure(1)
    fig.savefig(name)
    matplotlib.pyplot.clf()

# Task 01: Retrieve Tweets
tweets = ...
# Task 02: Create dataframe 
df = ...
# Task 03: Pre-process Tweets
df['cleaned_tweets'] = ...
# Task 04: Retrieve sentiments
df['sentiment'] = ...
# Task 05: Classify Tweets
classified_tweets = ...
# Task 06: Create Word Cloud
create_word_cloud(...)