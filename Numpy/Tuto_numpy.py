import numpy as np

#Create a 1D array 

array1 = np.array([1,2,3,4,5])
#print("array1 = ", array1, type(array1))
#print(array1.shape)

#Create a 2D array
array2 = np.array([ [1,2], [3,4], [5,6] ])
#print("array2 = ", array2, type(array2))
#print(array2.shape)

#Create a 3D array
array3 = np.array([ [ [1,2],[3,4],[5,6] ], [ [10,20],[30,40],[50,60] ] ])
#print("array 3 = ", array3, type(array3))
#print(array3.shape)

#Create an array with random values
random_array = np.random.randint(low=10, high=99, size=(4,2,2)) # choose the number of values and their shape
#print("random array de shape(",random_array.shape,"): \n"
#        random_array, type(random_array))

random_array2 = np.random.randint(low= [10,100], high=[99,1000], size=(4,2,2)) # you can also choose multiple values for each dimensions
#print("random array de shape(",random_array2.shape,"): \n",
#        random_array, type(random_array2))

norm_array = np.random.rand(2,2)
#print("norm_array = ", norm_array)

# table o zero
zero_array = np.zeros((2,4,6))
#print("zero_array = ", zero_array)

# Creation with specific datas
spe_array = np.arange(start=0, stop=100, step=10)
#print("spe_array = ", spe_array)

# Create matrice identity
identity_array = np.identity(4)
#print("identity_array = ",identity_array)



############## Manipulation ##############
mon_array = np.array([1,2,3,4,5,6])
print("mon_array", mon_array)

#ajout de valeur en 1D
appended_array = np.append(mon_array,[10,20,30])
print("appended_array", appended_array)

#array 2D
mon_array2D = np.array([ [1,2], [3,4], [5,6] ])
print("mon_array2D", mon_array2D)

# ajout en 2D sur axe 0
appended_array2D = np.append(mon_array2D,[[10,20],[30,40]], axis=0) #il faut renseigner l'option axis pour donner la dimension, sinon il aplanira en 1 seule dimension
print("appended_array2D", appended_array2D)

# ajout en 2D sur axe 1
appended_array2D2 = np.append(mon_array2D,[[10,20],[30,40],[50,60]], axis=1) #il faut renseigner l'option axis pour donner la dimension, sinon il aplanira en 1 seule dimension
print("appended_array2D2", appended_array2D2)

#pour supprimer des array
before_removed = np.random.randint(low=30, high=60, size=10)
print(before_removed)
removed_array = np.delete(before_removed, obj=[1,2,3,4,5])
print(removed_array)

#reshape array
rand_array = np.random.randint(low=10, high=20, size=(3,2))
print(rand_array)
reshape_array = np.reshape(rand_array, newshape=(2,3))
print(reshape_array)
#2D => 1D
new_shape_array = np.reshape(rand_array, newshape=(6,))
print(new_shape_array)
#1D => 2D
rand_array2 = np.random.randint(low=10, high=20, size=10)
print(rand_array2)
reshape_array2 = np.reshape(rand_array2, newshape=(5,2))
print(reshape_array2)

# numpy fournis la dimension -1 dans un reshape
rand_array3 = np.random.randint(low=10, high=20, size=(4,2))
print(rand_array3)
print(rand_array3.shape)
reshape_array3 = np.reshape(rand_array3, newshape=(-1,4))
print(reshape_array3)
print(reshape_array3.shape)

#aplanir array 2D
print(np.ndarray.flatten(rand_array3))
print(np.matrix.flatten(rand_array3))

#trriage des array
rand_array4 = np.random.randint(low=10, high=20, size=(4,3))
print(rand_array4)
print("tri selon axe 0 : \n", np.sort(rand_array4, axis=0))
print("tri selon axe 1 : \n", np.sort(rand_array4, axis=1))

#rotation d'array
rotate_array = np.random.randint([[10,20],[30,40]])
print(rotate_array)
print("rotation anti horaire:\n", np.rot90(rotate_array, k=1, axis=(0,1)))
print("rotation horaire:\n", np.rot90(rotate_array, k=1, axis=(1,0)))
print("rotation 2x horaire:\n", np.rot90(rotate_array, k=2, axis=(1,0)))
print("rotation 3x anti horaire:\n", np.rot90(rotate_array, k=3, axis=(0,1)))


############## Opérations Matricielle ##############

mat = np.randint(low=1, high=10, size=(3,3))
mat2 = np.randint(low=10, high=20, size=(3,3))
print(mat)
print(mat2)

#Addition
print("addition =\n", mat + mat2)
print("addition =\n", np.add(mat, mat2))

#Soustraction
print("soustraction =\n", mat - mat2)
print("soustraction =\n", np.substract(mat, mat2))

#multiplication
mat3 = np.randint(low=1, high=10, size=(3,2))
mat4 = np.randint(low=10, high=20, size=(2,3))
print(mat3)
print(mat4)
#print("multiplication =\n", mat3 * mat4) si taille égales
print("multiplication =\n", np.matmul(mat3, mat4))
print("multiplication =\n", np.dot(mat3, mat4))


