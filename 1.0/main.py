# Import files
from speech_module import SpeechModule

# Import libraries
import json
settings = json.load(open("settings/settings.json"))


SpeechModule(settings)