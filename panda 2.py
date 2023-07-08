#slicien array : to see particular range of numbers than use sliceing in array..

import numpy as np
arr = np.array([3,5,6,7,8,9,222,2,2,2])
print(arr[1:5])
print(arr[4:])
print(arr[:4])
print(arr[-3:-1])
print(arr[1:5:2])
print(arr[::2])