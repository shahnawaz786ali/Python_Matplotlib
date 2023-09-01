import random
import matplotlib.pyplot as plt
import numpy as np

x=np.random.randint(100,size=(100))
y=np.random.randint(100,size=(100))

colors=np.random.randint(100,size=(100))
size=np.random.randint(500,size=(100))

plt.scatter(x,y,c=colors,s=size,alpha=0.7) #s=size c=color alpha for transparency
plt.show()