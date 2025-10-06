# Exercise 1: Converting Lists into Dictionaries
keys = ['Ten', 'Twenty', 'Thirty'] 
values = [10, 20, 30]
test=zip(keys,values)
print(list(test))  # [('Ten', 10), ('Twenty', 20), ('Thirty', 30)]
#V1 methode avec une boucle
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

#  Exercise 2: Cinemax #2 total cost
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

#if age<3: free
#from 3 to 12 : $10*
#>=13 :$15
total_cost=0
for name, age in family.items():
    if age<3:
        price=0
    elif 3<=age<=12:
        price=10
    else:
        price=15
    print(f"{name} has to pay ${price}")
    total_cost+=price
print(f"The total cost of the family is ${total_cost}") 
#bonus
input_family=input("Enter the names and ages of family members," \
"separated by commas (e.g., 'rick 43,beth 13,morty 5,summer 8'):  ")
family2={}  
for member in input_family.split(","):
    name, age=member.split()
    family2[name]=int(age)
print(family2)

#  Exercise 3: Zara
brand={
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}
print(brand)
print('\n')

brand['number_stores']=2
print(brand)
print('\n')

sentence0=f"The clients of Zara are {brand['type_of_clothes'][0]}, {brand['type_of_clothes'][1]} and {brand['type_of_clothes'][2]}."
print(sentence0)
sentence=f"Zara's clients are mainly {', '.join(brand['type_of_clothes'])}." # problème car cite 'home'
print(sentence)
print('\n')

brand.update({'country_creation':'Spain'})
print(brand)
print('\n')

if 'international_competitors' in brand.keys():
    brand['international_competitors']= brand['international_competitors'] + ['Desigual']
print(brand)
print('\n')
del brand['creation_date']
print(brand)
print('\n')

print(brand['international_competitors'])
print(brand['international_competitors'][-1])
print('\n')
print(brand['major_color']['US'])
print('\n')
print(len(brand.keys()))
print('\n')
print(brand.keys())
print('\n')

# Exercise 4 : Some Geography



# Exercise 5 : Random



# Exercise 6 : Let’s create some personalized shirts !



# Exercise 7 : Temperature Advice



# Exercise 8: Pizza Toppings


