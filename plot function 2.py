import matplotlib.pyplot as plt
import numpy as np

a=np.arange(0,10,0.5)

plt.plot(a, "ro-", a**3, "g^--", a**2, "k.:")

plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Plot")

plt.show()