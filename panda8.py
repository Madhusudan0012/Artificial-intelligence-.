#flags: bolloen value provide karta he ...
#advance attribute :

import numpy as np

#example 2 :
x = np.array[[0,1,2],[3,4,5],[6,7,8],[9,10,11]]
print('our array is :',x)
rows = np.array([0,0],[3,3])
cols = np.array([0,2],[0,2])
y = x[rows,cols]
print ('The Corner Elements of this array are:', y)