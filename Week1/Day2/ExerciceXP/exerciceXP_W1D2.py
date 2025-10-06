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

# bonus
more_on_zara={'creation date':1975, 'number_stores':7000}
brand_updated={**brand, **more_on_zara} # fusion de deux dictionnaires
print(brand_updated)
#ou bien
brand.update(more_on_zara)
print(brand)


# Exercise 4 : Some Geography
def describe_city(city, country="Unkown"):
    print(f"{city} is in {country}.")

describe_city("Reykjavik", "Iceland")
describe_city("Paris")

# Exercise 5 : Random
import random
def fun_run(number_between_1_and_100):
    random_number=random.randint(1,100)
    if number_between_1_and_100==random_number:
        print("Congratulations! You guessed the number!")
    else:
        print(f"Sorry, the number was {random_number}. Better luck next time!")

fun_run(50)
fun_run(10)

# Exercise 6 : Let’s create some personalized shirts !
def make_shirt(size,text):
    """this function prints the size of a shirt and the text printed on it"""
    print(f"The size of the shirt is {size} and the text is '{text}'")

make_shirt("M","Yes we cat")

def make_shirt(size="L",text="I love python"):
    """this function prints the size of a shirt and the text printed on it"""
    print(f"The size of the shirt is {size} and the text is '{text}'")

make_shirt()
make_shirt(size="M")
make_shirt(text="Yes we cat")
make_shirt(size="small", text="Hello!")

# Exercise 7 : Temperature Advice
def get_random_temp():
    random_temp=random.randint(-10,40)
    # radom_temp=random.uniform(-10,40) # pour un float
    return random_temp
    

def main():
    temp=get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")
    if temp<0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif 0<=temp<16:
        print("Quite chilly! Don’t forget your coat")
    elif 16<=temp<23:
        print("Nice weather.")
    elif 24<=temp<=32:
        print("A bit warm, stay hydrated.")   
    else:
        print("It’s hot! stay cool.")

main()

# Exercise 8: Pizza Toppings

toppings=[]
added_topping=""
while added_topping!="quit":
    added_topping=input("what topping would you add? (enter quit when you're finished)")
    print(f"we'll add {added_topping} to your pizza")
    if added_topping!="quit":
        toppings.append(added_topping)
print(f"your pizza has the following toppings: {', '.join(toppings)}")
total_cost=10+2.5*len(toppings)
print(f"the total cost of your pizza is ${total_cost}")





