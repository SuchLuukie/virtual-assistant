# Import files
from commands_module import CommandsModule

# Import libraries
import json

class TextProcessingModule:
	def __init__(self, speech_module):
		self.speech_module = speech_module
		self.commands_module = CommandsModule()
		self.load_settings()


	def process_text(self, text):
		if not self.includes_wake_trigger(text):
			return

		result = self.extract_command(text)

		if result is None:
			self.speech_module.text_to_speech(self.command_not_recognised_message)
			return

		self.speech_module.text_to_speech(result)



	def extract_command(self, text):
		keywords = self.extract_command_keywords(text)
		keywords = keywords.replace(".", "")
		keywords = keywords.replace(",", "")
		keywords = keywords.lstrip()

		for command in self.commands_module.commands_dictionary:
			for command_keyword in command["keywords"]:
				if keywords in command_keyword:
					class_method = getattr(CommandsModule, command["command"])
					result = class_method(self.commands_module)
					return result

		return None


	def extract_command_keywords(self, text):
		index = text.find(self.wake_trigger) + len(self.wake_trigger)
		return text[index:]


	def includes_wake_trigger(self, text):
		return self.wake_trigger in text.lower()


	def load_settings(self):
		self.settings = json.load(open("settings.json"))

		self.wake_trigger = self.settings["wake_trigger"]
		self.command_not_recognised_message = self.settings["command_not_recognised_message"]