# Import files
from distutils.command.clean import clean
from posixpath import split
from commands.webScraping import WebScraping
from commands.small_talk.small_talk import SmallTalk
from commands.math.math import Math
from commands.math.unit_conversion import UnitConversion
from commands.math.currency_conversion import CurrencyConversion

# Import libraries
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import geocoder
import pytz


class Commands:
	def __init__(self, settings, uuid, operators):
		self.uuid = uuid
		self.settings = settings
		self.operators = operators
		self.web_scraping = WebScraping(self.settings)
		self.geolocator = Nominatim(user_agent="athena_virtual_assistant")

		# Extensions of commands for more organisation
		self.small_talk = SmallTalk(self.log_command, self.uuid)
		self.math = Math(self.log_command, self.uuid, self.operators)
		self.conversion_unit = UnitConversion(self.log_command, self.uuid)
		self.conversion_currency = CurrencyConversion(self.log_command, self.uuid, self.web_scraping)

	def log_command(self, uuid, command, info = ""):
		time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

		log_file = open('logs/commands.log', 'a')
		log_file.write(f"{time}, UUID: {uuid}, Command: {command}, {info}\n")
		log_file.close()


	# * Done
	def get_current_time(self, text):
		if "in " in text.lower():
			long_lat = self.get_lon_lat_from_text(text)
		else:
			long_lat = None

		if long_lat is None:
			current_time = datetime.now()
			clean_time = str(current_time.strftime("%I %M %p"))
			response = f"It's {clean_time}"

			self.log_command(self.uuid, "get_current_time", "timezone: local")
		
		else:
			location = text[text.index("in ")+3:]
			tf = TimezoneFinder()
			
			capital_tz = tf.timezone_at(lng=long_lat[0], lat=long_lat[1])
			tz = pytz.timezone(self.get_proper_timezone(capital_tz))
			
			time = datetime.now(tz)
			clean_time = str(time.strftime("%I %M %p"))
			response = f"It's {clean_time} in {location}"

			self.log_command(self.uuid, "get_current_time", f"timezone: {capital_tz}")

		return response

	# ? Slightly inaccurate when asking for states. Other than that, done
	def weather_forecast(self, text):
		if "in " in text.lower():
			long_lat = self.get_lon_lat_from_text(text)
		else:
			long_lat = geocoder.ip("me").latlng
			long_lat = long_lat[::-1]

		forecast = self.web_scraping.weather_map_api(long_lat)
		self.log_command(self.uuid, "weather_forecast", f"Location: {long_lat[0]}, {long_lat[1]}")

		return forecast


	def get_lon_lat_from_text(self, text):
		text = text[text.index("in ")+3:]
		geocode = self.geolocator.geocode(text)
		return [geocode.longitude, geocode.latitude]


	def get_proper_timezone(self, arg):
		timezones = pytz.all_timezones
		for timezone in timezones:
			if arg.lower() in timezone.lower():
				return timezone