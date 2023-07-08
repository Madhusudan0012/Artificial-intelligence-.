#binary search :
import numpy as np
arr = np.array([6,7,8,9])
x = np.searchsorted(arr ,7)
print(x)

#search from the right side 

import numpy as np 
arr = np.array([6,7,8,9])
x = np.searchsorted(arr , 7 , side='right ')
print(x)

#multiple Values :
import numpy as np
arr = np.array([1,3,5,7])
x = np.searchsorted(arr,[2,4,6])
print(x)