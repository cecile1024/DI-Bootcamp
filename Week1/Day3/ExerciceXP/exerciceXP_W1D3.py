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

# Exercise 4 : Afternoon at the Zoo
