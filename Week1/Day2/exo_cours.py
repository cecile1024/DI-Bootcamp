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

# challenge 2
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keys = ["name", "salary"]   
del sample_dict[keys[0]]
del sample_dict[keys[1]]
print(sample_dict)

my_books = {
  "title": "Harry Potter",
  "author": "JK Rowling",
}

print(my_books.items())
print(type(my_books.items()))
print(list(my_books.items()))

# challenge loops dictionnary

# my_dictio={}
# i=0
# while word!="quit":
#     word=input("give me a word")
#     i+=1
#     my_dictio[i]=word
#     if word=="quit"
#     break