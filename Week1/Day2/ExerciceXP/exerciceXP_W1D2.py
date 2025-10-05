# Exercise 1: Converting Lists into Dictionaries
keys = ['Ten', 'Twenty', 'Thirty'] 
values = [10, 20, 30]
test=zip(keys,values)
print(list(test))  # [('Ten', 10), ('Twenty', 20), ('Thirty', 30)]
#V1 methode bourrin avec range et len
my_dict={}
for i in range(len(keys)):
    my_dict[keys[i]] =values[i]
print(my_dict)  
#V2 avec la fonction zip
my_dict2=dict(zip(keys,values))
print(my_dict2)
#V3 avec une comprehension de dictionnaire
my_dict3={k:v for k,v in zip(keys,values)}
print(my_dict3) 

#  Exercise 2: Cinemax #2


#  Exercise 3: Zara


# Exercise 4 : Some Geography



# Exercise 5 : Random



# Exercise 6 : Let’s create some personalized shirts !



# Exercise 7 : Temperature Advice



# Exercise 8: Pizza Toppings


