#slicing the array

import numpy as np

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12]])

print("the array given looks like")
print(array)
print("now accessing the elements of the array")
print(array[0,0])
print(array[0,1])
print(array[2,0])

print(array[:, 1:3])
#selecting only column

print(array[:, 1])

print("Arthemetic operation in Array")

newArray = np.array([12,4,6,8])
print(newArray *2)
print(newArray -7)
print(newArray +3)
print(newArray / 2)
print(np.sqrt(newArray))
#can use np.round to round and np.floor to round down as well as np.ceil to round up

print("Vactorized math functions")

radii = np.array([1,2,3])
radii2 = np.array([4,5,6])

print(np.pi * radii **2)
print(radii + radii2)
print(radii - radii2)
print(radii * radii2)
print(radii ** radii2)

print("Comparasion operators")

scores = np.array([91,55,100,73,82,64,42])

print(scores == 100)
print(scores < 50)
print(scores > 50)

scores[scores < 50] = 0
print(scores)

