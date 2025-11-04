import matplotlib.pyplot as plt
import numpy as np

x=([25,30,32,25])
y=([21,22,24,32])

plt.plot(x,color='r')
plt.plot(y,color="y")

plt.grid()
plt.ylabel("income")
plt.xlabel("year")
plt.show()