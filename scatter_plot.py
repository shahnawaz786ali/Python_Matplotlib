import random
import matplotlib.pyplot as plt
import numpy as np

x=np.random.randint(50,size=(10))
y=np.random.randint(100,size=(10))

colors=np.array(["red","green","blue","yellow","pink","black","orange","purple",
                    "white","hotpink"])
size=np.random.randint(500,size=(10))

plt.scatter(x,y,c=colors,s=size) #s=size c=color
plt.show()