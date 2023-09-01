import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,4,8,12])
y=np.array([4,8,12,19])

plt.plot(x,y)

font={"family":"serif","color":"red","size":15}
font2={"family":"serif","color":"black","size":10}

plt.title("Speed-Distance Graph",fontdict=font,loc="left")
plt.xlabel("Time",fontdict=font2)
plt.ylabel("Distance",fontdict=font2)

plt.show()
