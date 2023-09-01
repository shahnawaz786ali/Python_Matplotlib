import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 2, 1)
plt.plot(x,y)
plt.title("plot1")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 2, 3)
plt.plot(x,y)
plt.title("plot3")

#plot 3:
x = np.array([0, 1, 2, 3])
y = np.array([5, 10, 20, 30])

plt.subplot(2, 2, 2)
plt.plot(x,y)
plt.title("plot2")

plt.suptitle("multiple plot")
plt.show()