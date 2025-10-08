# OOP Inheritance course
# I. Inheritance
# Inheritance is the process by which one class takes on the attributes and methods of another. 
# Newly formed classes are called child classes, and the classes that child classes are 
# derived from are called parent classes.
# For example, in real life, Dog is a child class of Animal, every Dog is an Animal, 
# but every Animal isn’t a Dog. Children inherit all of the parent’s attributes and behaviors 
# but can also specify different behavior to follow.
# To make a class inherit from another one, simply add it in round brackets on class definition:

class Animal():
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        print(f"{self.name} barked, WAF !")


# Inheritance is when a class uses code constructed within another class. 
# Classes called child classes or subclasses inherit methods and variables from parent classes 
# or base classes.

class Animal():
    def __init__(self, type, number_legs, sound):
        self.type = type
        self.number_legs = number_legs
        self.sound = sound

    def make_sound(self):
        print(f"I am an animal, and I love saying {self.sound}")

class Dog(Animal):
    pass

rex= Dog("dog", 4, "wouaf")
print('This animal is a:', rex.type)
# >> This animal is a dog

print('This dog has', rex.number_legs , ' legs')
# >> This dog has 4 legs

print('This dog makes the sound ', rex.sound)
# >> This dog makes the sound wouaf

rex.make_sound()
# >> I am an animal, and I love saying wouaf


# We have created a Dog object rex that uses the method and attributes of the Animal class 
# even though we did not define those methods and attributes in the Dog child class.

class Animal():
    def __init__(self, type, number_legs, sound):
        self.type = type
        self.number_legs = number_legs
        self.sound = sound

    def make_sound(self):
        print(f"I am an animal, and I love saying {self.sound}")

class Dog(Animal):
    def fetch_ball(self):
        print("I am a dog, and I love fetching balls")

rex = Dog('dog', 4, "Wouaf")
print('This animal is a:', rex.type)
# >> This animal is a: dog

rex.fetch_ball()
# >> I am a dog, and I love fetching balls

roger = Animal('Roger', 4, "Grr")
roger.fetch_ball()
# >> AttributeError: 'Animal' object has no attribute 'fetch_ball'

# This is because the method fetch_ball() belongs only to the Dog child class, 
# and not the Animal parent class.

# II . Overriding Parent Methods
# When you create the same method inside the child class, you override the parent class method.
# It’s important to note that child classes override or extend the functionality of parent classes. 
# The child class will have all the parent class’s functions, plus his functions.

class Animal():
    def __init__(self, type, number_legs, sound):
        self.type = type
        self.number_legs = number_legs
        self.sound = sound

    def make_sound(self):
        print(f"I am an animal, and I love saying {self.sound}")

class Dog(Animal):
    def fetch_ball(self):
        print("I am a dog, and I love fetching balls")

    def make_sound(self):
        print("I am an DOGGG !!! WOUAFFF!!")

rex = Dog('dog', 4, "Wouaf")
rex.make_sound()
# >> I am an DOGGG !!! WOUAFFF!!

# III. The super() Function
# With the super() function, you can gain access to inherited methods that have been overwritten 
# in a class object.

class Animal():
    def __init__(self, type, number_legs, sound):
        self.type = type
        self.number_legs = number_legs
        self.sound = sound

class Dog(Animal):
    def __init__(self, type, number_legs, sound, fetch_ball):
        super().__init__(type, number_legs, sound)
        # Or : Animal.__init__(self,type, number_legs, sound)
        self.fetch_ball = fetch_ball

rex = Dog('dog', 4, "wouaf", True)
print('This animal is a:', rex.type)
# >> This animal is a dog

print('This dog has', rex.number_legs , ' legs')
# >> This dog has 4 legs

print('This dog makes the sound ', rex.sound)
# >> This dog makes the sound wouaf

print('Does this dog fetchs balls ? ', rex.fetch_ball)
# >> Does this dog fetchs balls ? True


# We use super() function before __init__() method. 
# We want to pull the content of __init__() method from the parent class into the child class.
# You can also specify from which class you want to use the super() function.

class MyClass(object):
    def func(self):
        print("I'm being called from the Parent class")


class ChildClass(MyClass):
    def func(self):
        print("I'm actually being called from the Child class")
        print("But...")
        # Calling the `func()` method from the Parent class.
        super(ChildClass, self).func()

my_instance_2 = ChildClass()
my_instance_2.func()
