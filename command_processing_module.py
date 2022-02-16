# Import files
from commands_module import CommandsModule

# Import libraries
import json

class CommandProcessingModule:
	def __init__(self, speech_module, settings):
		self.settings = settings
		self.speech_module = speech_module
		self.commands_module = CommandsModule(self.settings)

		self.wake_trigger = self.settings["wake_trigger"]


	def process_command(self, text):
		if text == "stop":
			self.speech_module.listen = False
			return

		print(text)