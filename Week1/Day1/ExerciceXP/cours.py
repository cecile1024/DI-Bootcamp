username = "John"
age = 36
print(username) #John

sentence = username + " is " + age + " years old"
print(sentence)

sentence_second = username + " is " + str(age) + " years old"
print(sentence_second)

sentence_third =  f"{username} is {age} years old"
print(sentence_third)


age_client_company = 45
print(age_client_company)
age_client_company = age_client_company + 1 #ajoute +1 a l'age
print(age_client_company)
age_client_company += 1 #ajoute +1 a l'age
print(age_client_company)

age_client_company *= 2 #multiplie l'age par 2 et on reassign
print(age_client_company)

# CONDITIONALS

if username == "John" : # si la condition est vraie, je rentre dans le if
    print("Bonjour John")
else : # sinon je rentre dans le else
    print("Bonjour autre personne")


amount_bank = 10000
car_price = 3000

if amount_bank >= car_price : 
    print("I buy the car")
    # amount_bank = amount_bank - car_price
    amount_bank -= car_price
    print(f"I have {amount_bank} euros left")
else :
    print("I don't buy the car")


amount_second_bank = 2000
car_price_second = 3000
scooter_price = 1000

if amount_second_bank >= car_price_second : 
    print("I buy the car")
    amount_second_bank -= car_price_second
    print(f"I have {amount_second_bank} euros left")
elif amount_second_bank >= scooter_price : 
    print("I buy the scooter")
    amount_second_bank -= scooter_price
    print(f"I have {amount_second_bank} euros left")
else :
    print("I buy nothing")


amount_third_bank = 900
car_price_third = 3000
scooter_price_third = 1000
computer_price = 500

if amount_third_bank >= car_price_third : 
    print("I buy the car")
    amount_third_bank -= car_price_third
    print(f"I have {amount_third_bank} euros left")
elif amount_third_bank >= scooter_price_third : 
    print("I buy the scooter")
    amount_third_bank -= scooter_price_third
    print(f"I have {amount_third_bank} euros left")
elif amount_third_bank >= computer_price : 
    print("I buy the computer")
    amount_third_bank -= computer_price
    print(f"I have {amount_third_bank} euros left")
else :
    print("I buy nothing")

height = 140
age = 10
name = "Mickey"

# si les 2 sont vraies, alors "I go to the rollercoaster"
if age >= 10 and height >= 140 :
    print("I go to the rollercoaster")
else :
    print("I'm too small")

# si l'un des deux est vrai
if age >= 15 or name == "Mickey" :
    print("I go to the rollercoaster")
else :
    print("I'm too small")

paid = True

if paid == True :
    print("I go to the rollercoaster")
else :
    print("I'm too small")

if paid :
    print("I go to the rollercoaster")
else :
    print("I'm too small")



# "hello"
# 2
# 3.5
# True/False


animals = ["cat", "dog", "rabbit"] #list
print(len(animals))

first_element_list = animals[0] # premier element : cat

last_element_list = animals[2]
last_element_list_second_option = animals[-1]
print(last_element_list)
print(last_element_list)


#boucle for, qui va boucler sur une liste de 0 a 4, elle va boucler 5 fois
for i in range(5):  #boucle for
    print("hello", i)



# i = 0 --> print("hello")
# i = 1 --> print("hello")
# .
# .
# .
# i = 4 --> print("hello")

# 5*1
# 5*2
# 5*3

for i in range(11) : 
    multiplication = f"5 x {i}"
    result = 5*i
    sentence = f"{multiplication} = {result}"
    print(sentence)

animals_farm = ["cat", "dog", "rabbit"]

for animal in animals_farm :
    print(f"j'ai un {animal} dans ma ferme")


# 1er boucle
# animal = "cat"

# 2e boucle
# animal = "dog"

# 3e boucle
# animal = "rabbit"

animals_farm_list = ["cat", "dog", "rabbit"]

#len(animals_farm_list) = 3
# boucler de [0,1,2]

for i in range(len(animals_farm_list)) :
    print(f"i : {i}")
    animals_farm_list[i] = animals_farm_list[i] + "s"

print(animals_farm_list)

# 1er boucle
# i = 0 

#2e boucle
# i = 1 --> print("hello")
# .
# .




list_fruit = ["pear", "apple", ["banana", "orange"]]
fruit_orange = list_fruit[2][1]

list_of_tuple = [(0, 'john'), (1, 'dave')]
friend = list_of_tuple[0] #(0, 'john')
friend_john = list_of_tuple[0][1]

animals_farm_list_second = ["cat", "dog", "rabbit"]

#enumerate cree une liste de tuple a partir d'une liste
#dans la boucle for, je destructure les elements des tuples, avec i representant l'index et animal 
# representant la valeur de l'element
# puis j'utilise les 2 variable (i et animal) pour manipuler la liste initiale
for i, animal in enumerate(animals_farm_list_second) :
    print(f"i : {i}")
    animals_farm_list_second[i] = animal + "s"

print("animals_farm_list_second", animals_farm_list_second)