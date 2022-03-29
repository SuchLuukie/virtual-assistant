# Import libraries
import json

class Conversion:
    def __init__(self, log_command, uuid):
        self.log_command = log_command
        self.uuid = uuid

        self.unit_conversion_dict = json.load(open("commands/math/unit_conversion.json"))


    def reverse_convert_units(self, text):
        return self.convert_units(text, True)


    def convert_units(self, text, reverse = False):
        amount = self.get_amount(text)
        if amount == None:
            amount = 1

        if reverse:
            second_unit, first_unit = self.get_unit(text)

        else:
            first_unit, second_unit = self.get_unit(text)
        

        category = self.get_category(first_unit, second_unit)
        equation = self.unit_conversion_dict["conversion_rates"][category][first_unit][second_unit].format(amount)
        result = eval(equation)
        
        if type(result) is float:
            return f"approximately {round(result, 2)} {second_unit}"
        
        else:
            return f"{result} {second_unit}"


    def get_unit(self, text):
        split_text = text.split(" ")
        units = []
        for idx, split in enumerate(split_text):
            if idx != 0:
                double_split = split_text[idx-1] + " " + split
                double_idk = self.get_unit_conversion(double_split)
                if double_idk != False:
                    units.append(double_idk)
                    continue
            
            idk = self.get_unit_conversion(split)
            if idk != False:
                units.append(idk)


        return units

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

    def get_unit_conversion(self, string):
        conversion_units = self.unit_conversion_dict["units"]
        for category in conversion_units:
            for unit in conversion_units[category]:
                for way_of_spelling in conversion_units[category][unit]:
                    if string.lower() == way_of_spelling:
                        return unit

        return False


    def get_category(self, first, second):
        conversion_units = self.unit_conversion_dict["units"]
        for category in conversion_units:
            if first in conversion_units[category] and second in conversion_units[category]:
                return category


    def check_if_conversion_unit(self, string):
        conversion_units = self.unit_conversion_dict["units"]
        for category in conversion_units:
            for unit in conversion_units[category]:
                for way_of_spelling in conversion_units[category][unit]:
                    if string.lower() == way_of_spelling:
                        return True

        return False