import matplotlib.pyplot as plt
import numpy as np 
y = np.array([78,89,90,78])
mylabels = ['apples', 'banana', 'lunda', 'anuj']
plt.pie( y , labels = mylabels )
plt.legend()
plt.show()
