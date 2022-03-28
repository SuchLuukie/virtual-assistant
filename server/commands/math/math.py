

class Math:
    def __init__(self, log_command, uuid, operators):
        self.log_command = log_command
        self.uuid = uuid
        self.operators = operators


    def math(self, text):
        self.log_command(self.uuid, "math")
        cleaned_string = self.get_cleaned_string(text)
        response = eval(cleaned_string)

        if type(response) == float:
            if (response).is_integer():
                response = int(response)
            else:
                response = round(response, 2)

        return str(response)


    def get_cleaned_string(self, text):
        split_text = text.split(" ")
        cleaned_string = ""

        for split in split_text:
            if self.check_if_int(split) or self.check_if_float(split):
                cleaned_string += split + " "

            if split in self.operators:
                if split == "x":
                    cleaned_string += "* "

                else:
                    cleaned_string += split + " "

        return cleaned_string[:-1]

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