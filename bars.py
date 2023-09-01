import random
import matplotlib.pyplot as plt
import numpy as np

x=np.random.randint(10,size=(10))
y=np.random.randint(10,size=(10))

plt.bar(x,y,color="red",width=0.5)
plt.show()