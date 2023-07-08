import matplotlib.pyplot as plt
import numpy as np 
y = np.array([78,89,90,78])
mylabels = ['apples', 'banana', 'lunda', 'anuj']
myexplode = [0.2,0,0,0]
plt.pie( y , labels = mylabels ,  explode = myexplode , shadow = True)
plt.show()
