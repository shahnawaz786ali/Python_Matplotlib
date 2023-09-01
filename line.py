import matplotlib.pyplot as plt
import numpy as np

ypoints=np.array([2,4,6,8])
ypoints2=np.array([1,3,5,7])
ypoints3=np.array([5,10,15,20])
ypoints4=np.array([7,12,15,30])

plt.plot(ypoints, ls="dotted",color="r",linewidth=3) #ls=linestyle
plt.plot(ypoints2, ls="dashed",color="g",lw=5)
plt.plot(ypoints3, ls="-.",color="b",lw=10)
plt.plot(ypoints4, ls="--",color="pink",lw=7)


plt.show()