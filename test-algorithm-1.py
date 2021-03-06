import pandas as pd
import numpy as np


# Get a pandas DataFrame object of all the data in the csv file:
df = pd.read_csv('tweets.csv')

# Get pandas Series object of the "tweet text" column:
text = df['tweet_text']

# Get pandas Series object of the "emotion" column:
target = df['is_there_an_emotion_directed_at_a_brand_or_product']

# The rows of  the "emotion" column have one of three strings:
# 'Positive emotion'
# 'Negative emotion'
# 'No emotion toward brand or product'

# Remove the blank rows from the series:
target = target[pd.notnull(text)]
text = text[pd.notnull(text)]

# Perform feature extraction:
from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
count_vect.fit(text)
counts = count_vect.transform(text)

# Train with this data with a Naive Bayes classifier:
from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()
nb.fit(counts, target)

# See what the classifier predicts for some new tweets:
predictions = nb.predict(counts)
<<<<<<< HEAD:test-algorithm-1.py
correct= sum(predictions == fixed_target)
incorrect= sum(predictions != fixed_target)
acc = correct/(len(fixed_target))
print(acc)
=======
correct_predictions = sum(predictions == target)
incorrect_predictions = 9092 - correct_predictions  # (there are 9,092 tweets in the csv)
print('# of correct predictions: ' + str(correct_predictions))
print('# of incorrect predictions: ' + str(incorrect_predictions))
print('Percent correct: ' + str(100.0 * correct_predictions / (correct_predictions + incorrect_predictions)))
>>>>>>> a85337990f2d389bd846bc203e53a58cbab4e5a7:test_algorithm_1.py
