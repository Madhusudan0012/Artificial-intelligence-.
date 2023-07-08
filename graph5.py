import matplotlib.pyplot  as plt 
import numpy as np
x = np.array([45,45,23,67,89,56,98])
y = np.array([78,89,34,56,67,67,78])
plt.title("Sports")
plt.xlabel("average")
plt.ylabel("calorie")
plt.plot(x)
plt.grid( color= 'green' , linestyle = '--' , linewidth = 0.5  )
plt.show()