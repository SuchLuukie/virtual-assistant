# Import files
from web_scraping_module import WebScrapingModule

# Import libraries
from datetime import datetime
import geocoder
import json

class CommandsModule:
	def __init__(self, settings):
		self.settings = settings
		self.web_scraping_module = WebScrapingModule()
		self.commands_dictionary = json.load(open("commands_dictionary.json"))


	def get_current_time(self):
		current_time = datetime.now()
		clean_time = str(current_time.strftime("%I %M %p"))
		return clean_time


	def weather_forecast(self):
		local_latlon = geocoder.ip("me").latlng
		forecast = self.web_scraping_module.weather_map_api(local_latlon)
		return forecast