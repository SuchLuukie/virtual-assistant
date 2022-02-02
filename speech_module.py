# Import libraries
import speech_recognition as sr

class SpeechModule:
	def __init__(self):
		self.mic = sr.Microphone()
		self.r = sr.Recognizer()

		self.listen_for_audio()


	def listen_for_audio(self):
		self.listen = True
		# Listen for audio, if audio is detected try to perform audio to text
		with self.mic as source:
			self.r.adjust_for_ambient_noise(source, duration=1)
			while self.listen:
				try:
					audio = self.r.listen(source)
					self.audio_to_text(audio)
			
				# If unable to perform audo to text, continue to listen
				except sr.UnknownValueError:
					continue

	def audio_to_text(self, audio):
		text = self.r.recognize_google(audio)
		print(text)