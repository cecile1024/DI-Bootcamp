# Exercise 1: Pets
class Pets():
    def __init__(self, animals):
        self.animals = animals
   
    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

bengal_obj=Bengal('chouchou',7)
chartreux_obj=Chartreux('Titi',3)
siamese_obj=Siamese('Mitch',9)
all_cats = [bengal_obj, chartreux_obj, siamese_obj]

sara_pets=Pets(all_cats)
sara_pets.walk()



# Exercise 2: Dogs

class Dog():
    def __init__(self, name, age, weight):
        self.name=name
        self.age=age
        self.weight=weight
    
    def bark(self):
        return "is barking"
    
    def run_speed(self):
        return self.weight/self.age*10
    
    def fight(self,other_dog):
        my_power=self.run_speed()*self.weight
        other_power=other_dog.run_speed()*other_dog.weight
        if my_power>other_power:
            return f'{self.name} wins'
        if my_power ==other_power:
            return f'drawn - no winner'
        else:
            return f'{self.name} loss and {other_dog.name} wins'

dog1=Dog('choupi',7,0.5)
dog2=Dog('Marcus',12,10)
dog3=Dog('Roxane',4,6)

print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))
print(dog2.fight(dog3))
    

# Exercise 3: Dogs Domesticated
# In a new file
# import the Dog class


# Exercise 4: Family and Person Classes