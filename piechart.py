import matplotlib.pyplot as plt
import numpy as np

x=np.array([30,20,40,10])
labels=["apple","orange","grapes","guava"]
myexplode=[0.2,0,0,0]
colors=["purple","red","orange","yellow"]

plt.pie(x,labels=labels,startangle=70,explode=myexplode,shadow=True,colors=colors)
plt.legend(title="4 Fruits")
plt.show()
