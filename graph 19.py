import matplotlib.pyplot as plt
import numpy as np 
y = np.array([78,89,90,78])
mylabels = ['apples', 'banana', 'lunda', 'anuj']
mycolors = ["black" , "hotpink" , "b" , "#4CAF50"]
plt.pie( y , labels = mylabels ,  explode = mycolors )
plt.show()
