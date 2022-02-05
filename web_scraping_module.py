# Import libraries
import requests
import json

class WebScrapingModule:
	def __init__(self):
		self.api_keys = json.load(open("api_keys.json"))
		self.settings = json.load(open("settings.json"))


	def weather_map_api(self, latlon):
		weather_map_api_key = self.api_keys["OpenWeatherMap"]

		forecast = requests.get("https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units={}".format(
			latlon[0], 
			latlon[1], 
			weather_map_api_key, 
			self.settings["measuring_system"]
		)).json()


		info = "{} degrees and a {}".format(round(forecast["main"]["temp"]), forecast["weather"][0]["main"])
		return info