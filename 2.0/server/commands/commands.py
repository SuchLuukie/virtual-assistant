# Import files
from distutils.command.clean import clean
from posixpath import split
from commands.webScraping import WebScraping

# Import libraries
from timezonefinder import TimezoneFinder
from countryinfo import CountryInfo
from datetime import datetime
import pycountry
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


	# For now only countries and gets the time for the capital
	# https://github.com/jannikmi/timezonefinder
	def get_current_time(self, text):
		if "in " in text.lower():
			country_name = self.find_country_from_text(text)
		else:
			country_name = None


		if country_name is None:
			current_time = datetime.now()
			clean_time = str(current_time.strftime("%I %M %p"))
			response = f"It's {clean_time}"

			self.log_command(self.uuid, "get_current_time", "local")
		
		else:
			country = CountryInfo(country_name)
			tf = TimezoneFinder()
			latitude, longitude = country.capital_latlng()
			
			capital_tz = tf.timezone_at(lng=longitude, lat=latitude)
			tz = pytz.timezone(self.get_proper_timezone(capital_tz))
			
			time = datetime.now(tz)
			clean_time = str(time.strftime("%I %M %p"))
			response = f"It's {clean_time} in {country.capital()}, {country_name}"

			self.log_command(self.uuid, "get_current_time", capital_tz)

		return response


	# TODO Improve forecast, bit weird with the speech and wrong forecast
	def weather_forecast(self, text):
		local_latlon = geocoder.ip("me").latlng
		forecast = self.web_scraping.weather_map_api(local_latlon)

		self.log_command(self.uuid, "weather_forecast",
		                 f"Location: {local_latlon[0]}, {local_latlon[1]}")
		return forecast


	def find_country_from_text(self, text):
		split_text = text.split(" ")
		# Double worded countries
		for idx in range(len(split_text)):
			try:
				possible_country = f"{split_text[idx]} {split_text[idx+1]}"
			except IndexError:
				break

			for country in pycountry.countries:
				if country.name.lower() == possible_country.lower():
					return country.name


		# Single worded countries
		for word in split_text:
			for country in pycountry.countries:
				if country.name.lower() == word.lower():
					return country.name
			
		return None

	def get_proper_timezone(self, arg):
		timezones = pytz.all_timezones
		for timezone in timezones:
			if arg.lower() in timezone.lower():
				return timezone