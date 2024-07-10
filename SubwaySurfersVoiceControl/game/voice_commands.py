import speech_recognition as sr

class VoiceCommands:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def get_command(self):
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)
            try:
                command = self.recognizer.recognize_google(audio, language="en-US")
                return command
            except sr.UnknownValueError:
                return None