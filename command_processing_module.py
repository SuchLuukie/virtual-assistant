# Import files
from distutils.command.clean import clean
from commands_module import CommandsModule
from intent_classifier_module import IntentClassifier

# Import libraries
import json
import re

class CommandProcessingModule:
	def __init__(self, speech_module, settings):
		self.settings = settings
		self.speech_module = speech_module
		self.commands_module = CommandsModule(self.settings)
		self.intent_classifier = IntentClassifier()

		self.operators = json.load(open("settings/operators.json"))
		self.wake_trigger = self.settings["wake_trigger"]


	# Main function that gets called when speech was recognised.
	def process_command(self, text):
		#If wake trigger is not in text don't look for commands
		if not self.wake_trigger.lower() in text:
			return

		# Simply exit program if stop is the text
		if text == "stop":
			self.speech_module.listen = False
			return

		# Call intent classifier for it's prediction
		prediction = self.intent_classifier.predict(text)

		# Check if the text is a math question by looking for integers and operators
		has_math = self.contains_math(text)

		answer = self.execute_command(text, prediction, has_math)
		return answer

	
	def execute_command(self, text, prediction, has_math):
		if has_math:
			return self.commands_module.math(self.clean_text_for_math(text))
		
		return getattr(self.commands_module, prediction)()


	# Check if there are integers or operators in a string.
	def contains_math(self, text):
		if re.search('\d', text):
			return True
		
		for operator in self.operators:
			if operator in text:
				return True
		
		return False


	# Cleans the text so only integers/floats and operators are in the text
	def clean_text_for_math(self, text):
		text = text.split(" ")

		clean_text = ""
		for element in text:
			if element in self.operators:
				clean_text += f" {element}"
			
			if re.search('\d', element):
				clean_text += f" {element}"
				
		return clean_text


	# Checks if a string is an integer
	def check_if_int(self, string):
		if s[0] in ('-', '+'):
			return s[1:].isdigit()
		return s.isdigit()