#shape function :
#resize the shape of the array 

import numpy as np
a = np.array([[1,2,3],[2,3,4]])
a.shape = (3,2)
print(a.shape)
b = a.reshape(3,2)
print(b)# arrange function :
#this function returns number of array dimensions 
import numpy as np
a = np.arrange(24)
a.ndim
b =a.reshape(2,4,3)
print(a)
print(b)
