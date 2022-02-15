# Import files
from web_scraping_module import WebScrapingModule

# Import libraries
from datetime import datetime
import geocoder
import json


class CommandsModule:
	def __init__(self, settings):
		self.settings = settings
		self.web_scraping_module = WebScrapingModule(self.settings)
		self.commands_dictionary = json.load(open("commands_dictionary.json"))


	def log_command(self, command, info):
		time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

		log_file = open('logs/commands.log', 'a')
		log_file.write(f"{time}, Command: {command}, {info}\n")
		log_file.close()


	def get_current_time(self):
		self.log_command("get_current_time", "")

		current_time = datetime.now()
		clean_time = str(current_time.strftime("%I %M %p"))
		return clean_time


	def weather_forecast(self):
		local_latlon = geocoder.ip("me").latlng
		forecast = self.web_scraping_module.weather_map_api(local_latlon)

		self.log_command("weather_forecast", f"Location: {local_latlon[0]}, {local_latlon[1]}")
		return forecast