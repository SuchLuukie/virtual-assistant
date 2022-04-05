# Import libraries
import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
import threading
import os

class Speech:
    def __init__(self, api_handler):
        self.api_handler = api_handler
        self.mic = sr.Microphone()
        self.r = sr.Recognizer()
        self.phrase_timeout_time = 6

        self.listen_thread = threading.Thread(target=self.listen_for_audio)
        self.listen_thread.daemon = True
        self.listen_thread.start()


    # Main function to start listening for audio for the text to speech
    def listen_for_audio(self):
        self.listen = True
        # Listen for audio, if audio is detected try to perform audio to text
        with self.mic as source:
            self.r.adjust_for_ambient_noise(source, duration=5)
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
        self.process_command(text.lower())


    # Function to perform text to speech using playsound library for audio
    def text_to_speech(self, text):
        print(text)
        tts = gTTS(text)
        tts.save("temp/temp.mp3")
        playsound("temp/temp.mp3")
        os.remove("temp/temp.mp3")


    # Main function that gets called when speech was recognised.
    def process_command(self, text):
        #If wake trigger is not in text don't look for commands
        if not "athena" in text:
            return

        text = text.replace("athena ", "")
        response = self.api_handler.command_request(text)
        if response == None:
            self.text_to_speech("Login timed out, please login again")
            self.listen = False
            return

        self.text_to_speech(response)