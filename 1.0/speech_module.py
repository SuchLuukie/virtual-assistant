# Import Files
from command_processing_module import CommandProcessingModule

# Import libraries
from playsound import playsound
import speech_recognition as sr
from gtts import gTTS
import json
import os


class SpeechModule:
	def __init__(self, settings):
		self.settings = settings
		self.text_processing_module = CommandProcessingModule(self, self.settings)
		self.mic = sr.Microphone()
		self.r = sr.Recognizer()

		self.phrase_timeout_time = self.settings["phrase_timeout_time"]

		self.listen_for_audio()


	# Function to perform text to speech using playsound library for audio
	def text_to_speech(self, text):
		tts = gTTS(text)
		tts.save("temp/temp.mp3")
		playsound("temp/temp.mp3")
		os.remove("temp/temp.mp3")


	# Main function to start listening for audio for the text to speech
	def listen_for_audio(self):
		self.listen = True
		# Listen for audio, if audio is detected try to perform audio to text
		with self.mic as source:
			self.r.adjust_for_ambient_noise(source, duration=1)
			while self.listen:
				try:
					audio = self.r.listen(source, phrase_time_limit=self.phrase_timeout_time)
					self.audio_to_text(audio)
			
				# If unable to perform audo to text, continue to listen
				except sr.UnknownValueError:
					continue


	# Recognize text from audio
	def audio_to_text(self, audio):
		text = self.r.recognize_google(audio)
		self.text_processing_module.process_command(text.lower())