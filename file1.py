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
print("Mean of the rainfalls in month  :", meanRainfall)

maxRainfall = np.max(rainfall)
print("the max amount of rainfall :", maxRainfall)

minRainfall = np.min(rainfall)
print("the min amount of rainfall : :", minRainfall)

totalRainfall = np.sum(rainfall)
print("Total amount of rainfall overall the month : ", totalRainfall)

# rainfall[1] = 0
# print(rainfall)

noRainfall = np.sum(rainfall == 0)
print("No of days with no rainfall : ",noRainfall)

heavyRainfall = np.sum( rainfall >= 30)
print("No of days with heavy rainfall :", heavyRainfall)

midRainfall = np.sum((rainfall < 30) & (rainfall >20))
print("No of days with mid rainfall : ", midRainfall)

rolling_3dayRainfall = []

for i in range(len(rainfall)-2):
    rolling_3daySum = rainfall[i] + rainfall[i+1] + rainfall [i+2]
    rolling_3dayRainfall.append(rolling_3daySum)

rolling_3dayRainfall = np.array(rolling_3dayRainfall)
print("3 days rolling rainfall :",rolling_3dayRainfall)
print("number of values: ", len(rolling_3dayRainfall))







