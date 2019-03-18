# Twitter_Sentiment_Analysis

This project involves
- accessing the twitter Application Programming Interface(API) using python
- estimate the public's perception (the sentiment) of a particular term or phrase
- analyze the relationship between location and mood based on a sample of twitter data


Files Descriptions:

twitterstream.py - Collect Livestream twitter data
term_sentiment.py - computes the sentiment for the terms that do not appear in the file AFINN-111.txt.
tweet_sentiment.py - computes the sentiment of each tweet based on the sentiment scores of the terms in the tweet
frequency.py - computes the term frequency histogram of the collected livestream twitter data.
happiest_state.py - Returns the name of the happiest state
top_ten.py - computes the ten most frequently occurring hashtags from the twitter data
