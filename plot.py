import matplotlib.pyplot as plt
import numpy as np

xpoints=np.array([3,5,7,9])
ypoints=np.array([6,10,20,50])
ypoints2=np.array([6,15,10,30])

plt.plot(xpoints,ypoints)
plt.plot(xpoints,ypoints2,":")
plt.show()