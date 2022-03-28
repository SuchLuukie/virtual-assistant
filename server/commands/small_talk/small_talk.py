# Import libraries
import random
import json
import csv

class SmallTalk:
    def __init__(self, log_command, uuid):
        self.log_command = log_command
        self.uuid = uuid

    def how_am_i(self, text):
        self.log_command(self.uuid, "how_am_i")
        responses = json.load(open("commands/small_talk/SmallTalk.json"))["how_am_i"]
        return random.choice(responses)

    
    def joke(self, text):
        self.log_command(self.uuid, "joke")
        with open("commands/small_talk/jokes.csv") as f:
            reader = csv.reader(f)
            return random.choice(list(reader))[-1]

    
    def greeting(self, text):
        return "Hello"