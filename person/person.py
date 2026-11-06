class Person:

    def __init__(self, speech, message):
        self.speech = speech
        self.message = message

    def speak(self):
        self.speech.speak("Человек", self.message)