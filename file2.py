import numpy as np

rainfall_2d = np.array (
    [
         [5, 12, 0, 0, 18, 25, 30, 10, 8, 0, 0, 15, 20, 22, 35, 40, 28, 18, 12, 5, 0, 0, 7, 14, 26, 33, 21, 19, 9, 4],  # District 1
    [0, 0, 8, 12, 5, 0, 18, 20, 22, 25, 30, 10, 8, 0, 0, 15, 20, 22, 35, 40, 28, 18, 12, 5, 0, 0, 7, 14, 26, 33],  # District 2
    [10, 15, 20, 25, 5, 0, 0, 12, 18, 22, 5, 0, 0, 8, 12, 5, 0, 18, 20, 22, 25, 30, 10, 8, 0, 0, 15, 20, 22, 35]  # District 3
    ]
)

print(rainfall_2d)

rolling_7day_2d = []

for districtwise in rainfall_2d:
    rolling_7day_district = []
    for i in range(len(districtwise)-7):
        rolling_7day_district.append(districtwise[i] + districtwise[i + 1] + districtwise[i + 2] + districtwise[i + 3] + districtwise[i + 4] + districtwise[i +5 ] + districtwise[i + 6] + districtwise[i + 7])
    rolling_7day_2d.append(rolling_7day_district)
rolling_7day_2d = np.array(rolling_7day_2d)
print("The rolling 7 day in 2d matrix seems like: ",rolling_7day_2d)