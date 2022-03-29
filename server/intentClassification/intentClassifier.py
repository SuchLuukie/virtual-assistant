# Import libraries
import json
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

        # Conversion unit info
        self.conversion_units = json.load(open("commands/math/unit_conversion.json"))["units"]
        self.conversion_currency = json.load(open("commands/math/currency_conversion.json"))

        # Train the intent classifier
        self.train()


    # prepare the text for intent classification
    def prepare_text(self, text):
        split_text = text.split(" ")
        for idx, split in enumerate(split_text):
            if split in self.operators:
                split_text[idx] = "OPERATOR"

            elif self.check_if_int(split) or self.check_if_float(split):
                split_text[idx] = "INTEGER"

            elif idx != 0:
                double_split = split_text[idx-1] + " " + split
                if self.check_if_conversion_unit(double_split):
                    del split_text[idx-1]
                    split_text[idx-1] = "CONVERSION_UNIT"
                    continue

                if self.check_if_conversion_currency(double_split):
                    del split_text[idx-1]
                    split_text[idx-1] = "CONVERSION_CURRENCY"
                    continue

            if self.check_if_conversion_unit(split):
                split_text[idx] = "CONVERSION_UNIT"

            if self.check_if_conversion_currency(split):
                split_text[idx] = "CONVERSION_CURRENCY"

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


    def check_if_conversion_unit(self, string):
        for category in self.conversion_units:
            for unit in self.conversion_units[category]:
                for way_of_spelling in self.conversion_units[category][unit]:
                    if string.lower() == way_of_spelling:
                        return True

        return False

    def check_if_conversion_currency(self, string):
        for currency in self.conversion_currency:
            for way_of_spelling in self.conversion_currency[currency]:
                if string.lower() == way_of_spelling:
                    return True

        return False
