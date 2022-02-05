import json

class TextProcessingModule:
	def __init__(self):
		self.load_settings()


	def extract_command(self, text):
		index = text.find(self.wake_trigger) + len(self.wake_trigger)
		return text[index:]


	def includes_wake_trigger(self, text):
		return self.wake_trigger in text.lower()


	def load_settings(self):
		self.settings = json.load(open("settings.json"))

		self.wake_trigger = self.settings["wake_trigger"]

TextProcessingModule()