class Animal:
    def speak(self):
        print('Animal Sound')
class Dog(Animal):
    def speak(self):
        print('BARKS')
class Cat(Animal):
    def speak(self):
        print("MEOW")

animals = [Dog(), Cat()]
for animal in animals:
    animal.speak()
