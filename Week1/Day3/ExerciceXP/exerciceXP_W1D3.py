# Exercise 1: Cats
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1=Cat("Bigou",15)
cat2=Cat("Nova",9)
cat3=Cat("Mishka",12)

def find_oldest_cat(cat1, cat2, cat3):
    # oldest=cat1
    # if cat2.age>oldest.age:
    #     oldest=cat2
    # if cat3.age>oldest.age:
    #     oldest=cat3
    # return [oldest.name,oldest.age] #oldest is n object of class Cat 
    oldest= max ([cat1,cat2,cat3], key=lambda cat: cat.age)
    return oldest

oldest_cat=find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} cat-years old")
# [oldest_cat_name, oldest_cat_age]=find_oldest_cat(cat1, cat2, cat3)
# print(f"The oldest cat is {oldest_cat_name}, and is {oldest_cat_age} cat-years old")


# Exercise 2 : Dogs
class Dog:
    def __init__(self,name, heigth):
        self.name=name
        self.heigth=heigth
    
    def bark(self):
        print(f"{self.name} goes woof!")
    
    def jump(self):
        print("{} jumps {}cm high!".format(self.name,self.heigth*2))

davids_dog=Dog("Bill",100)
sarahs_dog=Dog("Woopy",50)

print(f"Sarah's dog is {sarahs_dog.name}, and is {sarahs_dog.heigth}cm high")
print(f"david's dog is {davids_dog.name}, and is {davids_dog.heigth}cm high")

davids_dog.bark()
davids_dog.jump()
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.heigth > sarahs_dog.heigth:
    print(f"{davids_dog.name} is bigger than {sarahs_dog.name}")
elif davids_dog.heigth < sarahs_dog.heigth:
    print(f"{davids_dog.name} is smaller than {sarahs_dog.name}")
else:
    print("Both dogs have the same size")

# Exercise 3 : Who’s the song producer?
# Goal: Create a Song class to represent song lyrics and print them.
class Song():
    def __init__(self,lyrics=[]):
        self.lyrics=lyrics

    def sing_me_a_song(self):
        for element in self.lyrics:
            print(element)

stairway = Song(["There s a lady who's sure", "all that glitters is gold",
                  "and she s buying a stairway to heaven"])
stairway.sing_me_a_song()


# Exercise 4 : Afternoon at the Zoo
class Zoo():
    # def __init__(self,zoo_name,animals=[]):
    #     self.zoo_name=zoo_name
    #     self.animals=animals

    def __init__(self,zoo_name):
        self.zoo_name=zoo_name
        self.animals=[]

    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            print(f"The animal {new_animal} is already in the zoo {self.zoo_name}")
    
    def get_animals(self):
        print(f"animals in the zoo are :{' ,'.join(my_zoo.animals)}")
          
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"The animal {animal_sold} was in the zoo {self.zoo_name} and has been sold.")
        else:
            print(f"This animal, the {animal_sold}, is not in the zoo {self.zoo_name}")
    
    def sort_animals(self):
        dict_animals={}
        for animal in self.animals:
            initiale=animal[0].upper()
            if initiale not in dict_animals:
               dict_animals[initiale]=[]
            dict_animals[initiale].append(animal)
        return dict_animals
        print(dict_animals)

    def get_groups(self):
        local_dict_one=self.sort_animals()
        local_dict_two=dict(sorted(local_dict_one.items()))
        for item in local_dict_two.items(): #.items met le dict sous forme de liste de tuples
            print(f"{item[0]}:{item[1]}")

my_zoo = Zoo("wildoo")
my_zoo.animals=["cat", "bird"]
print(my_zoo.animals)
print(my_zoo.zoo_name)

my_zoo.add_animal("mouse")
print(my_zoo.animals)

my_zoo.add_animal("cat") #duplicated cat to test condition
print(my_zoo.animals)

my_zoo.get_animals()

my_zoo.sell_animal('pig')
my_zoo.sell_animal('mouse')
print(my_zoo.animals)

my_zoo.add_animal("cochon")
my_zoo.add_animal("squirle")
my_zoo.add_animal("snake")
my_zoo.add_animal("dragonfly")
my_zoo.add_animal("superstar")

dictio=my_zoo.sort_animals()
print(dictio)

my_zoo.get_groups()
