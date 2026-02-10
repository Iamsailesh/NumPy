import numpy as np

#broadcasting allows numpy to perform oprations on array with different 
# shapes by virtually expanding dimesions to match large array shaps

array1 = np.array([[1,2,3,4]])
array2 = np.array([[1],[2],[3],[4]])
array3 = np.array([[1,2],[2,3],[3,4],[4,5]])
array4 = np.array([[2,3,4,5],[4,5,6,6]])

print(array1.shape)
print(array2.shape)
# print(array1)
# print(array2)
print(array3 * array4)
print(array1 * array2) 

#the above code may generate error as operands could not be broadcast together
#as for that if row of first array is 1 then column of second array should 1 either of equal shapes of array