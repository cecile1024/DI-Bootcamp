# hard but elegant version with dictionary comprehension
user_word=input("enter a word:")
position={letter: [i for i,l in enumerate(user_word) if l ==letter] for letter in set(user_word)}
print(position)

# print(set(user_word)) user_word=magnifique
# {'n', 'f', 'i', 'm', 'u', 'e', 'g', 'a', 'q'}
# list(enumerate(user_word)) user_word=magnifique
#[(0, 'm'), (1, 'a'), (2, 'g'), (3, 'n'), (4, 'i'), (5, 'f'), (6, 'i'), (7, 'q'), (8, 'u'), (9, 'e')]
# output {'e': [9], 'm': [0], 'i': [4, 6], 'a': [1], 'u': [8], 'f': [5], 'g': [2], 'n': [3], 'q': [7]}

# autre version plus facile avec boucle
user_word_two=input("enter a word:")
positions = {}
for index, letter in enumerate(user_word_two):
    if letter not in positions:
        positions[letter]=[] # créer une liste pour cette lettre
        positions[letter].append(index) # ajouter l'index corrspondant à la liste   
    else:
        positions[letter].append(index) # ajouter l'index corrspondant à la liste    

print(positions)


