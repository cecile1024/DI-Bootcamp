# challenge 1
number=int(input("Enter a number: "))
length=int(input("Enter a length: "))

list_of_multiples=[]
for i in range(1,length+1):
    list_of_multiples.append(number*i)
print(list_of_multiples)



# challenge 2
string=input("Enter a string with lots of duplicated letters, like ttiiiittllleeee: ")
new_string=string[0]
for i in range(1,len(string)+1):
    if string[i-1]!=string[i:i+1]: # bizarre car string[i-1]!=string[i]:    ne marche pas : 
    # IndexError: string index out of range, pourtant string[2] et string[2:3] renvoie la meme lettre
        new_string+=string[i:i+1]
print(new_string)
# NB : Pourquoi string[i:i+1] fonctionne : Les tranches (slices) en Python, comme string[i:i+1], 
# ne déclenchent pas d'erreur quand l’index est en dehors de la chaîne.
# Si i == len(string), alors : string[len(string):len(string)+1]  # 
# → c’est une chaîne vide, pas une erreur.      


#challenge 2 / autre version
string=input("Enter a string with lots of duplicated letters, like ttiiiittllleeee: ")
new_string=string[0]
for i in range(1,len(string)):  # on s'arrete a len(string)-1   
    if string[i-1]!=string[i]: 
        new_string+=string[i]
print(new_string)




