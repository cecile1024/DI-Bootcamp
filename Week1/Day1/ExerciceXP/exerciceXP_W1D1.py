# Exercise 1 : Hello World
print(("Hello world\n")*5)

# Exercise 2 : Some Math
calcul=(99**3)*8
print(calcul)

# Exercise 3 : What’s your name ?
my_name="Cecile"
user_name=input("What is your name ?")
if my_name==user_name:
    print("amazing! We have the same name!")
else:print(f"Nice to meet you {user_name}")

# Exercise 4 : Tall enough to ride a roller coaster
user_height=int(input("What is your height in cm?"))
if user_height>=145:
    print("Your are tall enough to ride.")
else:print("Sorry, you've to grow a little bit more to ride")

# Exercise 5 : Favorite Numbers
my_fav_numbers={3,7,11,12,17,47}
my_fav_numbers.add(9)
my_fav_numbers.add(23)
print(my_fav_numbers)
my_fav_numbers.discard(23)
friend_fav_numbers={4,65,83,103}
our_fav_numbers=my_fav_numbers|friend_fav_numbers 
# or : our_fav_numbers=my_fav_numbers.union(friend_fav_numbers)   
print(our_fav_numbers)

# Exercise 6: Tuple
my_tuple=(1,2,3,4,5)
print(my_tuple)
# my_tuple[5]=10 # TypeError: 'tuple' object does not support item assignment
# Tuples are immutable, you cannot change their values once defined.

# Exercise 7: List Manipulation
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket)
basket.remove("Banana")
print(basket)
basket.remove("Blueberries")
print(basket)
basket.append("Kiwi")
print(basket)
basket.insert(0,"Apples")
print(basket)
print(basket.count("Apples")) # 2
basket.clear()
print(basket) # [] verifier que la liste est bien vide

# Exercise 8 : Sandwich Orders
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", 
                   "Avocado sandwich", "Pastrami sandwich", 
                   "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
print(sandwich_orders)




