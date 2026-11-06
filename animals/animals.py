class Dog:

    def __init__(self, speech, message):
        self.speech = speech
        self.message = message

    def speak(self):
        self.speech.speak("Собака", self.message)


class Cat:

    def __init__(self, speech, message):
        self.speech = speech
        self.message = message

    def speak(self):
        self.speech.speak("Кошка", self.message)