# Daily challenge: Old MacDonald’s Farm

class Farm():
    def __init__(self,farm_name):
        self.farm_name=farm_name
        self.animals={}
    
    def add_animal(self,animal_type, count=1):
        if animal_type in self.animals.keys():
            self.animals[animal_type]+=1
        else:
            self.animals.update({animal_type:count})
    
    def get_info(self):
        print(f"{self.farm_name}")
        for animal in self.animals.items(): #.items met le dict sous forme de liste de tuples
            print(f"{animal[0]} : {animal[1]}")
        print("E-I-E-I-O!")
# Bonus
    def get_animal_types(self):
         sorted_animals=sorted(self.animals.keys())
         print(f"{sorted_animals}")
         return sorted_animals # list of animal type in alpha order

    def get_short_info(self):
        animals_type=self.get_animal_types() # return a list of animal type in alpha order
        # mettre au pluriel les types d'animaux concernés

        for animal in animals_type:
            if self.animals[animal]>1:
                index=animals_type.index(animal)
                animals_type[index]+='s'
        print(f"{self.farm_name} has {', '.join(animals_type[0:-1])} and {animals_type[-1]}")



my_farm=Farm("Cecile's farm")
my_farm.add_animal("cat",3)
my_farm.add_animal("rabbit",5)
my_farm.add_animal("dog",2)
my_farm.add_animal("duck",10)
# print(f"{my_farm.animals}")
my_farm.get_info()
my_farm.get_animal_types()
my_farm.get_short_info()