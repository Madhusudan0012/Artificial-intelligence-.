import matplotlib.pyplot  as plt 
import numpy as np
x1 = np.array([1,4,6,7])
y1 = np.array([5,6,7,8])
x2 = np.array([4,6,7,0])
y2 = np.array([5,7,8,9])
plt.plot(x1,y1,x2,y2)
plt.show()