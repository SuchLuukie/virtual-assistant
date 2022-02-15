# Import files
from commands_module import CommandsModule

# Import libraries
import json
import re

class TextProcessingModule:
	def __init__(self, speech_module, settings):
		self.settings = settings
		self.speech_module = speech_module
		self.commands_module = CommandsModule(self.settings)

		self.operators = json.load(open("settings/operators.json"))
		self.wake_trigger = self.settings["wake_trigger"]
		self.command_not_recognised_message = self.settings["command_not_recognised_message"]


	def process_text(self, text):
		if text == "stop":
			self.speech_module.listen = False
			return

		possible_commands = self.commands_module.commands_dictionary.copy()
		print(text)
		print(possible_commands)

		# If text doesn't contain wake trigger it is not a command
		if not self.includes_wake_trigger(text):
			return

		types = self.extract_command_keywords(text)


#	def extract_command(self, text):
#		keywords = self.extract_command_keywords(text)
#		keywords = keywords.replace(".", "")
#		keywords = keywords.replace(",", "")
#		keywords = keywords.lstrip()
#
#		for command in self.commands_module.commands_dictionary:
#			for command_keyword in command["keywords"]:
#				if command_keyword in keywords:
#					class_method = getattr(CommandsModule, command["command"])
#					result = class_method(self.commands_module)
#					return result
#
#		return None

	# Function to extract different types (Integers, Operators)
	def extract_keywords_type(self, text):
		types = ["str"]

		# Check if string contains any integers
		if re.search("\d", text):
			types.append("int")

		# Check if string contains an operator
		for operator in self.operators:
			if operator in text:
				types.append("operator")

		# Return all the types that are in the text.
		return types


	def extract_command_keywords(self, text):
		index = text.find(self.wake_trigger) + len(self.wake_trigger)
		return text[index:]


	def includes_wake_trigger(self, text):
		if len(text) <= len(self.wake_trigger):
			return False

		return self.wake_trigger.lower() in text.lower()