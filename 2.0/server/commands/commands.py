# Import files
from commands.webScraping import WebScraping

# Import libraries
from timezonefinder import TimezoneFinder
from datetime import datetime
from geotext import GeoText
import geocoder
import pytz


class Commands:
	def __init__(self, settings, uuid):
		self.uuid = uuid
		self.settings = settings
		self.web_scraping = WebScraping(self.settings)

	def log_command(self, uuid, command, info = ""):
		time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

		log_file = open('logs/commands.log', 'a')
		log_file.write(f"{time}, UUID: {uuid}, Command: {command}, {info}\n")
		log_file.close()


	# ! currently only works with integers and not floats
	# ! Unsafe using eval, just temporary
	def math(self, text):
		return str(eval(text))


	# TODO
	def greeting(self, text):
		return "Hello!"


	# For now only countries
	def get_current_time(self, text):
		country = GeoText(text.title()).countries[0]
		print(country)
		timezones = pytz.all_timezones
		print(timezones)
		timezone = [tz for tz in timezones if country in tz]
		print(timezone)

		self.log_command(self.uuid, "get_current_time", "")

		current_time = datetime.now()
		clean_time = str(current_time.strftime("%I %M %p"))
		return clean_time


	# TODO Improve forecast, bit weird with the speech and wrong forecast
	def weather_forecast(self, text):
		local_latlon = geocoder.ip("me").latlng
		forecast = self.web_scraping.weather_map_api(local_latlon)

		self.log_command(self.uuid, "weather_forecast",
		                 f"Location: {local_latlon[0]}, {local_latlon[1]}")
		return forecast
