# Import libraries
import pandas as pd
from currency_converter import CurrencyConverter
from currency_symbols import CurrencySymbols
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB  # Import Naive Bayes


class IntentClassifier:
    def __init__(self, operators):
        self.operators = operators

        # Read the CSV file
        self.data = pd.read_csv('intentClassification/intentClassificationData.csv')

        # Train the intent classifier
        print([CurrencySymbols.get_symbol(sign)
              for sign in CurrencyConverter().currencies])
        self.train()


    # prepare the text for intent classification
    def prepare_text(self, text):
        split_text = text.split(" ")
        for idx, split in enumerate(split_text):
            if split in self.operators:
                split_text[idx] = "OPERATOR"

            elif self.check_if_int(split) or self.check_if_float(split):
                split_text[idx] = "INTEGER"

        return " ".join(split_text)

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
        prepared_text = self.prepare_text(text)
        print(prepared_text)
        return self.clf.predict(self.count_vect.transform([prepared_text]))[0]


    def check_if_int(self, string):
        try:
            a = int(string)
            return True

        except ValueError:
            return False

    def check_if_float(self, string):
        try:
            a = float(string)
            return True

        except ValueError:
            return False