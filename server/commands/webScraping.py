# Import libraries
import requests
import json

class WebScraping:
	def __init__(self, settings):
		self.settings = settings
		self.api_keys = json.load(open("api_keys.json"))


	# Gets the forecast from the OpenWeatherMap API
	def weather_map_api(self, lonlat):
		weather_map_api_key = self.api_keys["OpenWeatherMap"]
		
		forecast = requests.get("https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units={}".format(
			lonlat[1],
			lonlat[0],
			weather_map_api_key,
			self.settings["measuring_system"]
		)).json()

		info = "{} degrees and {}".format(
			round(forecast["main"]["temp"]), forecast["weather"][0]["description"])
		return info


	def currency_rates_api(self):
		currency_rates_api_key = self.api_keys["ExchangeRateAPI"]

		currency_rates = requests.get("http://api.exchangeratesapi.io/v1/latest?access_key={}".format(
			currency_rates_api_key
		)).json()

		return currency_rates
