class Animal:  # Parent class (superclass)
    location = "Australia"

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Speaking now...")


class Dog(Animal):  # Dog inherits from Animal (Dog is a subclass of Animal)
    def speak(self):  # We *override* the speak method (more on this later)
        super().speak()  # we are using the speak functions of the parent class
        print("Woof!")


# # Create objects:
d = Dog("Rover")
d.speak()
# print(d.location)
