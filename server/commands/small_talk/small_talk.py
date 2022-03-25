# Import libraries
import random
import json
import csv

class SmallTalk:
    def __init__(self, settings, uuid):
        self.uuid = uuid
        self.settings = settings

    def how_am_i(self, text):
        responses = json.load(open("commands/small_talk/SmallTalk.json"))["how_am_i"]
        return random.choice(responses)

    
    def joke(self, text):
        with open("commands/small_talk/jokes.csv") as f:
            reader = csv.reader(f)
            return random.choice(list(reader))[-1]