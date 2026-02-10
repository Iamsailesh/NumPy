import numpy as np

#aggregrate array= summarize data and return single value
array1 = np.array([[1,2,3,4],[5,6,7,8]])
print(np.sum(array1))
print(np.mean(array1))
print(np.std(array1)) #sdt deviation
print(np.var(array1)) #variance
print(np.argmin(array1)) #returns the position of minimun value

print(np.sum(array1, axis = 1))