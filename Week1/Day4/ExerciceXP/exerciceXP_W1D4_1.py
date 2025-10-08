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
class Person():
    def __init__(self, first_name,age,last_name=""):
        self.first_name=first_name
        self.age=age
        self.last_name=last_name
    def is_18(self):
        if self.age>=18:
            return True
        else:
            return False

class Family():
    def __init__(self, last_name, members=[]):
        self.last_name=last_name
        self.members=members
    
    def born(self,first_name,age):
        person=Person(first_name, age,self.last_name)
        self.members.append(person)
          
    def check_majority(self, first_name):
        list_members=list(self.members)
        for index in range(0,len(list_members)):
            if list_members[index].first_name==first_name:
                majority=self.members[index].is_18()
                if majority:
                    print(f"{first_name}, you are over 18, your parents accept that you will go out with your friends")
                else:   
                    print(f"Sorry {first_name}, you are not allowed to go out with your friends.")
            
    def family_presentation(self):
        print(f"{self.last_name}")
        for member in self.members:
            print(f"{member.first_name}, {member.age}")




famille=Family('Dupont')
print(f"{famille.last_name}")
# print(f"{famille.members}")

JP=famille.born('JP',34)
Melissa=famille.born('Melissa',2)
# print(f"{famille.members}")

famille.check_majority('Melissa')
famille.check_majority('JP')

famille.family_presentation()


