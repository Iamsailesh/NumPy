import numpy as np
# print(np.__version__)

# arr1 = np.array[2,3,4]
# print(arr1)

#Numpy array of daily rainfall values
#Single dimension array
rainfall = np.array([
    5, 12, 0, 0, 18, 25, 30,
    10, 8, 0, 0, 15, 20, 22,
    35, 40, 28, 18, 12, 5,
    0, 0, 7, 14, 26, 33,
    21, 19, 9, 4
])

print(rainfall)
print("Number of days in the month: ",rainfall.size)

meanRainfall = np.mean(rainfall)
print("Mean of the rainfalls in month is :", meanRainfall)

maxRainfall = np.max(rainfall)
print("the max amount of rainfall is", maxRainfall)

minRainfall = np.min(rainfall)
print("the min amount of rainfall is :", minRainfall)

totalRainfall = np.sum(rainfall)
print("Total amount of rainfall overall the month is: ", totalRainfall)

rainfall[1] = 0
print(rainfall)

noRainfall = np.sum(rainfall == 0)
print("No of days with no rainfall is: ",noRainfall)

heavyRainfall = np.sum( rainfall >= 30)
print("No of days with heavy rainfall is :", heavyRainfall)




