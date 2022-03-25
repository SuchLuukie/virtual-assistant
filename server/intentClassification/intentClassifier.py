import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB  # Import Naive Bayes


class IntentClassifier:
    def __init__(self):
        # Read the CSV file
        self.data = pd.read_csv('intentClassification/intentClassificationData.csv')

        # Train the intent classifier
        self.train()


    # Trains the intent classifier
    def train(self):
        X_train, y_train = self.data['text'], self.data['intent']
        self.count_vect = CountVectorizer()

        X_train_counts = self.count_vect.fit_transform(X_train)
        tfidf_transformer = TfidfTransformer()

        # Calculates tf-idf for the text
        X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
        self.clf = MultinomialNB().fit(X_train_tfidf, y_train)


    # Predicts intent from text
    def predict(self, text):
        return self.clf.predict(self.count_vect.transform([text]))[0]
