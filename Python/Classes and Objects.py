class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return self.name + " says Woof!"

my_dog = Dog("Buddy")
print(my_dog.bark())


#This code defines a Dog class with a constructor (__init__) and a method (bark) and creates a my_dog object.