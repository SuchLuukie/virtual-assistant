# Import libraries
from datetime import datetime
import json

class CommandsModule:
	def __init__(self):
		self.commands_dictionary = json.load(open("commands_dictionary.json"))


	def get_current_time(self):
		current_time = datetime.now()
		clean_time = str(current_time.strftime("%I %M %p"))
		return clean_time