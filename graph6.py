import matplotlib.pyplot  as plt 
import numpy as np
#plot 1
x = np.array([45,45,23,67])
y = np.array([78,89,34,56])
plt.subplot(1,2,1)
plt.plot(x,y)
#plot 2
x = np.array([45,65,29,67])
y = np.array([78,89,34,56])
plt.subplot(1,2,2)
plt.plot(x,y)
plt.show()