import numpy as np
print(np.__version__)
#2.3.3
my_array1=np.array([1,2,3])
print(f'my array1 is {my_array1} with this shape {my_array1.shape}')

my_array2=np.array([[1],[2]])
print(f'my array2 is {my_array2} with this shape {my_array2.shape}')

my_array3D=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[11,12,13,14],[15,16,17,18],[19,20,21,22]]])
print(f'my array3D is {my_array3D} with this shape {my_array3D.shape}')
#  with this shape (2, 3, 4) : 2 blocs, chaque bloc de 3 lignes et 4 colonnes

array_ex1=np.array([1,2,3,4,5])
array_ex2=np.array([1,2,3,4,5,6])
array_ex2_reshaped1=np.reshape(array_ex2,(3,2))
print(array_ex2_reshaped1)
array_ex2_reshaped2=np.reshape(array_ex2,(2,-1))
print(array_ex2_reshaped2)

a1=np.array(range(1,11))
print(a1)
a2=np.reshape(a1,(2,-1))
print(a2)

image=np.array([[22,22,22],[21,22,34],[22,45,54]])
print(image)
valid_image=np.array(image==22)
print(valid_image)


a3=np.array([[1,2,3],[4,5,6]])
result=a3[a3>7]
print(result)

array = np.array([10, 20, 30, 40, 50])
print("First element:", array[0])

# Slicing (accessing multiple elements)
print("First three elements:", array[:3])

# a55=np.array([[range(0,6)],[range(10,16)],[range(20,26)],[range(30,36)],[range(40,46)],[range(50,56)]])
# pb ci-dessus : shape : (6,1) donc 6 lignes avec chaque fois une seule colonne, contenant des objets : les range
# a55=np.array([list(range(0,6)),
#               list(range(10,16)),
#               list(range(20,26)),
#               list(range(30,36)),
#               list(range(40,46)),
#               list(range(50,56))])

# ou bien avec arrange et braodcasting
print(np.arange(0, 60, 10)[:, None])
a55 = np.arange(0, 60, 10)[:, None] + np.arange(6)
# rows: 0,10,20,30,40,50  +  cols: 0..5  => matrice 6x6

print(f'matrice de depart 6x6 : {a55}')# matrice 6x6
print(a55.shape)

print(f'elements 1ere ligne, 4e et 5e col {a55[0,3:5]}') #1ere ligne, element 3e et 4e col
print(f'elements suivants à partir de la 5e lg et à partir de la 5e col jusque la fin {a55[4:,4:]}') # à partir du 5eme element jusquà la fin, à partir de la 5e colonne
print(f'elements de toute la ligne de la 3eme col : {a55[:,2]}')
print(f'1 element sur 2 à partir de la 3e ligne, pour 1 col sur 2 : {a55[2::2,::2]}')

# Boolean indexing
print("Elements greater than 25:", a55[a55 > 25])

# Fancy indexing (using a list of indices)
print("Select specific elements:", a55[[1, 3]]) # renvoie la 2eme et 4 eme ligne
print("Select other specific elements:", a55[[(1,4),(3,0)]])

new_array=np.array(list(range(1,11)))
print(new_array)
print(new_array.shape)
# 1. Basic Indexing: Create an array of 10 elements and access the 5th element in it.
print(f' le 5eeme élément est : {new_array[4]}')
# 2. Basic Slicing: From the same array, extract a slice containing the 3rd to the 8th elements.
print(f'slice containing the 3rd to the 8th element : {new_array[2:8]}')
# 3. Boolean Indexing: Create an array of 6 random integers between 10 and 50. Print the elements that are greater than 30.
import random
narray=np.array([random.randint(10,50) for _ in range(6)])
print(f'matrice ligne element entre 10 et 50: {narray}')
print(f'element plus grand que 3° : {narray[narray>30]}')
# 4. Fancy Indexing: From the same array, use fancy indexing to access the 2nd, 4th, and 6th elements.
print(f'fancy indexing to acces elements 2, 4 et 6 : {narray[[1,3,5]]}')

rand = np.random.randint(10, 50, 6)
print(rand)
print(rand[rand>30])

x = np.array([1, 2, 3, 4, 5, 6, 7])
new = np.random.permutation(x)
print(new)

x = np.arange(10)
print(x)

# Creating two arrays
a = np.array([[1], [2], [3]])
b = np.array([1, 2, 3])

# Adding the two arrays
result = a + b

print("Array a: ", a)
print("Array b:", b)
print("Broadcasted Addition:", result)