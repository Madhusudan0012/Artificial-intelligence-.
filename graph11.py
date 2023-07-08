import matplotlib.pyplot  as plt 
import numpy as np
x = np.array([45,45,23,67])
y = np.array([78,89,34,56])
sizes = np.array([34,34,37,39,53,34,68,78,78,78,5,44])
plt.scatter(x,y,s =sizes , alpha=0.5)
plt.show()