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
