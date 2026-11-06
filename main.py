from behaviors import SpeechBehavior
from person import Person
from robot import Robot
from animals import Dog, Cat


speech = SpeechBehavior()

dog = Dog(speech, "Гав-гав!")
cat = Cat(speech, "Мяу!")
person = Person(speech, "Привет, меня зовут Алекс!")
robot = Robot(speech, "Я робот!")

dog.speak()
cat.speak()
person.speak()
robot.speak()

print("\nДополнительные режимы:")

speech.shout("Кошка", "Мяу!")
speech.whisper("Робот", "Привет")