import matplotlib.pyplot as plt

plt.plot([1,2,3,4],"g", linewidth=20)
plt.plot([3,6,8,9],"ro", markersize=10)
plt.plot([2,3,5,7],"b+", markersize=20)
plt.plot([10,20,30,40],"g", [2,3,4,5], "ro")

plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Plot")

plt.show()