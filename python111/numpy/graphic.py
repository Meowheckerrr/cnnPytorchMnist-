import numpy as np
import matplotlib.pyplot as plt

uniform_arr = np.random.random(10000)
normal_arr = np.random.normal(0, 1, 10000)
randint_arr = np.random.randint(1, 7, size=6)
print(uniform_arr)
print(normal_arr)
print(randint_arr)

# Random graphic 
fig = plt.figure()
ax = plt.axes()
ax.hist(uniform_arr, bins=30) # 30 blocks
plt.show()

# Normal graphic
fig = plt.figure()
ax = plt.axes()
ax.hist(normal_arr, bins=30)
plt.show()
