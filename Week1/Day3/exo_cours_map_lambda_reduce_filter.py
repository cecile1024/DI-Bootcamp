# fonctions : lambda, map, reduce, filter

# Introduction
# In this lesson, we will delve into Python’s functional programming features,
#  focusing on lambda functions and the map, reduce, and filter functions. 
# Functional programming is a programming paradigm that treats computation 
# as the evaluation of mathematical functions and avoids changing-state and mutable data. 
# It emphasizes the use of pure functions that avoid side effects, which can lead to more predictable 
# and bug-resistant code.
# Python, while not a purely functional programming language, supports many functional programming concepts
#  and allows developers to adopt some of these principles for cleaner and more efficient code. 
# By understanding these functional programming tools, you can write code that is not only concise 
# but also easier to test and debug.

# What you will learn
# How to use the map() function to apply a function to each item in an iterable.
# How to use the filter() function to filter items out of an iterable based on a condition.
# How to use the reduce() function to apply a function of two arguments cumulatively to the items of a sequence.
# How to create and use lambda functions for quick and concise function definition.


# Prerequisites
# Basic understanding of Python functions.
# Familiarity with Python’s list and dictionary data types.


# Ressources
# Python’s Map Function Explained.# https://www.youtube.com/watch?v=8q2vICb89ys :
# Lambda(), Map(), Filter() functions in Python :https://medium.com/analytics-vidhya/lambda-map-filter-functions-in-python-4c03679dd747
# Python’s Lambda Expressions, Map and Filter :https://towardsdatascience.com/understanding-the-use-of-lambda-expressions-map-and-filter-in-python-5e03e4b18d09

# https://www.w3schools.com/python/python_lambda.asp
# https://realpython.com/python-map-filter-reduce/
# https://www.programiz.com/python-programming/methods/built-in/filter
# https://www.programiz.com/python-programming/methods/built-in/map
# https://www.programiz.com/python-programming/methods/built-in/reduce

#nb : filter & map n'afficheront que l'adresse memoire : 
# il faut leur demander d'afficher le contenu de l'adresse meoire avec list
# map : function to apply a function to each item in an iterable.
def upper_string(s): # fonction mettre en majuscule
    return s.upper()

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_object = map(upper_string, fruit)

print(list(map_object)) # besoin de mettre list pour afficher le résultat, 
# sinon juste l'allocation memoire apparait
# >> ['APPLE', 'BANANA', 'PEAR', 'APRICOT', 'ORANGE']


# The filter() function
# Similar to map(), filter() takes a function object and an iterable and creates a new list.

# As the name suggests, filter() forms a new list that contains only the elements that satisfy a particular condition, this condition is the function we passed as an argument, if it returns True, the element will be added to the new list, else it won’t.
# For example, the following snippet will return only the strings starting with an A.

def starts_with_A(s):
    return s[0] == "A"

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filtered_object = filter(starts_with_A, fruit)

print(list(filtered_object))
# >> ['Apple', 'Apricot']


# The functools.reduce() Function
# reduce() works differently than map() and filter(). It does not return a new list 
# based on the function and iterable we’ve passed. Instead, it returns a single value.
# For example, the sum function is a reducing operation, 
# it takes a list as an argument and returns a single number.
# A function passed to reduce needs to receive two arguments 
# that will represent the first and the second element of the iterable, 
# and then the second and the third, and then the third and the fourth, etc…
# For example, a snippet that recreates the sum function:

# rend une fonction glissante/iterative pour l'appliquer sur tous les elements successifs d'un iterable
from functools import reduce #module functools

def sum_numbers(first, second): 
    return first+second

my_list = [1, 3, 5, 7]
reduced_list = reduce(sum_numbers, my_list)

print(reduced_list)
# >> 16


# Lambda functions
# Lambda functions are “one-line functions”, 
# they only receive arguments and return a value, 
# and they don’t need to be stored in variables (but they can !).
# Here is the syntax of a lambda function:
# lambda arg1, arg2: value_returned
# For example, a function that returns a string in capital letters:

lambda s: s.upper()

# You can also store this function into a variable if you want to reuse it:

my_function = lambda s: s.upper()
# This is the same as doing: 
def my_function(s):
    return s.upper()

# Those functions can be handy when using maps, filter, and reduce operations because they allow you to create it quickly. For example, let’s recreate the previous snippets using lambda functions.

# The map example:
fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_object = map(lambda s: s.upper(), fruit)
print(list(map_object))

# The filter example:
fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filtered_object = filter(lambda s: s[0] == "A", fruit)
print(list(filtered_object))

# The reduce example:
from functools import reduce
my_list = [1, 3, 5, 7]
reduced_list = reduce(lambda first, second: first+second, my_list)

# Challenge
people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
# Using map and filter, try to say hello to everyone who's name is less than or equal to 4 letters

short_names=filter(lambda name: len(name)<=4, people)

salutations=map(lambda s:f"hello {s}!", short_names)
for cc in salutations:
    print(cc)

# Conclusion
# This lesson has introduced you to powerful functional programming concepts in Python 
# that facilitate concise and readable code. By mastering lambda, map, reduce, and filter, 
# you enhance your ability to write high-quality Pythonic code that effectively leverages 
# Python’s capabilities for functional programming.