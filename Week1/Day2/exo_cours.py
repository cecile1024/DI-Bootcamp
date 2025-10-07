# shirts = [
#   {
#     'name': 'Awesome T-shirt 3000',
#     'size': 'S',
#     'price': 20
#   },
#   {
#     'name': 'Awesome T-shirt 3000',
#     'size': 'M',
#     'price': 25
#   },
#   {
#     'name': 'Awesome T-shirt 3000',
#     'size': 'L',
#     'price': 30
#   },
# ]

# res=shirts[1].items()
# print(res)
# print(type(res))
# print(list(res))


# chalenge Access the value of key history

sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

print(sample_dict['class']['student']['marks']['history'])
# Output: 80    
# or with get
print(sample_dict.get('class').get('student').get('marks').get('history'))
# Output: 80
# or with a function
def get_value(d, key):
    if key in d:
        return d[key]
    for k, v in d.items():
        if isinstance(v, dict):
            item = get_value(v, key)
            if item is not None:
                return item
    return None
print(get_value(sample_dict, 'history'))
# Output: 80
# or with a function and exception
def get_value2(d, key):
    try:
        return d[key]
    except KeyError:
        for k, v in d.items():
            if isinstance(v, dict):
                item = get_value2(v, key)
                if item is not None:
                    return item
    return None
print(get_value2(sample_dict, 'history'))
# Output: 80

def get_nested(d, keys, defautl=None):
    for k in keys:
        d=d.get(k,{})
        return d or defautl
history_value=get_nested(sample_dict, ['class','student','marks','history'])
print(history_value)
#output: 80


# challenge 2
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keys = ["name", "salary"]   # keys to remove
del sample_dict[keys[0]]
del sample_dict[keys[1]]
print(sample_dict)
#ou bien
keys_to_remove = ["name", "salary"]
#reconstuire le dictionnaire sans les clés à supprimer
new_dict = {k: v for k, v in sample_dict.items() if k not in keys_to_remove}
print(new_dict)
#ou bien
for key in keys_to_remove:
        sample_dict.pop(key)
print(sample_dict)
#output {'age': 25, 'city': 'New york'}


my_books = {
  "title": "Harry Potter",
  "author": "JK Rowling",
}

print(my_books.items())
print(type(my_books.items()))
print(list(my_books.items()))

# challenge loops WHILE dictionnary

# my_dictio={}
# i=0
# while word!="quit":
#     word=input("give me a word")
#     i+=1
#     my_dictio[i]=word
#     if word=="quit"
#     break

my_dictio={}
while True: 
    key=input("Enter key (or 'quit' to stop):")
    if key.lower()=='quit':  # attention methode lower importante pour bien comparer les 'quit'
        break
    value=input("Enter value:")
    my_dictio[key]=value
print(my_dictio)


