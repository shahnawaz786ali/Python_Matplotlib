import matplotlib.pyplot as plt
import numpy as np

ypoints=np.array([3,6,10,20])
xpoints2=np.array([3,5,10,15])
ypoints2=np.array([1,10,5,15])

plt.plot(ypoints, marker="o") # if xpoints is not given by default it starts from 0
plt.plot(xpoints2,ypoints2, marker="s", ms=10, mec="r",mfc="g")
plt.show()