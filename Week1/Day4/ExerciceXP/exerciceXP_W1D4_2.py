# Exercise 3: Dogs Domesticated
# In a new file
# import the Dog class

import random
from exerciceXP_W1D4_1  import  Dog
# Create a class called PetDog that inherits from the Dog class.
class PetDog(Dog):
# Add a trained attribute to the __init__ method, with a default value of False.
# trained means that the dog is trained to do some tricks.
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained=trained
# Implement a train() method that prints the output of bark() and sets trained to True.
    def train(self):
        print(self.bark())
        self.trained=True
# Implement a play(*args) method that prints “ all play together”.
# *args on this method is a list of dog instances.
    def play(self,*args):
        self.petDog_Friends=list(*args)
        sentence=', '.join(self.petDog_Friends)
        print(f"{self.name}, {sentence}, all play together")
# Implement a do_a_trick() method that prints a random trick if trained is True.
# Use this list for the ramdom tricks:
# tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
# Choose a rendom index from it each time the method is called.
    def do_a_trick(self,tricks=["does a barrel roll", 
                                "stands on his back legs", "shakes your hand", "plays dead"]):
        self.tricks=tricks
        index=random.randint(1,len(self.tricks))-1
        if self.trained:
            print(f"{self.name} {self.tricks[index]}")
# Create instances of the PetDog class and test the train(), play(*args), and do_a_trick() methods.

petDog1=PetDog('Riri',3,2)
petDog2=PetDog('Cachou',8,4)
petDog3=PetDog('Moustache',1,1)
petDog1.train()
petDog1.play([petDog3.name,petDog2.name])
petDog1.do_a_trick()