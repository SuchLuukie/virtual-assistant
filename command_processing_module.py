# Import files
from commands_module import CommandsModule
from intent_classifier_module import IntentClassifier

# Import libraries
import json

class CommandProcessingModule:
	def __init__(self, speech_module, settings):
		self.settings = settings
		self.speech_module = speech_module
		self.commands_module = CommandsModule(self.settings)
		self.intent_classifier = IntentClassifier()

		self.wake_trigger = self.settings["wake_trigger"]


	# Main function that gets called when speech was recognised.
	def process_command(self, text):
		print(text)
		#If wake trigger is not in text don't look for commands
		if not self.wake_trigger.lower() in text:
			return

		# Simply exit program if stop is the text
		if text == "stop":
			self.speech_module.listen = False
			return

		# TODO
		# Check if the text is a math question by looking for integers and operators

		# Call intent classifier for it's prediction
		prediction = self.intent_classifier.predict(text)
		print(f"Prediction: {prediction}")