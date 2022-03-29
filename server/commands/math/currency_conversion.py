# Import libraries
import time
import json
from currency_converter import CurrencyConverter
from datetime import datetime, timedelta


class CurrencyConversion:
    def __init__(self, log_command, uuid, web_scraping):
        self.log_command = log_command
        self.uuid = uuid
        self.web_scraping = web_scraping

        self.currency_conversion = json.load(open("commands/math/currency_conversion.json"))
        self.conversion_rates = self.get_currency_rates()


    def convert_units(self, text, reverse= False):
        self.log_command(self.uuid, "convert_currency")
        amount = self.get_amount(text)
        if amount == None:
            amount = 1

        try:
            if reverse:
                second_currency, first_currency = self.get_currency(text)

            else:
                first_currency, second_currency = self.get_currency(text)

            result = amount / self.conversion_rates[first_currency] * self.conversion_rates[second_currency]

        except (KeyError, ValueError):
            return "I'm not quite sure what you mean"

        if type(result) is float:
            return f"approximately {round(result, 2)} {self.currency_conversion[second_currency][0]}"

        else:
            return f"{result} {self.currency_conversion[second_currency][0]}"


    def get_currency_rates(self):
        rates = json.load(open("commands/math/currency_conversion_rates.json"))
        old_time = datetime.utcnow() + timedelta(hours=-12)

        if not rates["timestamp"] > time.mktime(old_time.timetuple()):
            rates = self.web_scraping.currency_rates_api()
            with open('commands/math/currency_conversion_rates.json', 'w') as outfile:
                json.dump(rates, outfile, indent=4)

        return rates["rates"]


    def get_currency(self, text):
        split_text = text.split(" ")
        currencies = []
        for idx, split in enumerate(split_text):
            if idx != 0:
                double_split = split_text[idx-1] + " " + split
                double_idk = self.get_currency_conversion(double_split)
                if double_idk != False:
                    currencies.append(double_idk)
                    continue

            idk = self.get_currency_conversion(split)
            if idk != False:
                currencies.append(idk)
        return currencies


    def get_amount(self, text):
        split_text = text.split(" ")
        for split in split_text:
            if self.check_if_int(split):
                return int(split)

            elif self.check_if_float(split):
                return float(split)

    # Checks if a string is an integer

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
        for currency in self.currency_conversion:
            for way_of_spelling in self.currency_conversion[currency]:
                if string.lower() == way_of_spelling:
                    return True

        return False


    def get_currency_conversion(self, string):
        for currency in self.currency_conversion:
            for way_of_spelling in self.currency_conversion[currency]:
                if string.lower() == way_of_spelling:
                    return currency

        return False