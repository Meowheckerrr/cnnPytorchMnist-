
import numpy as np

arr = np.arange(1, 10)

print(arr.reshape(3, -1))  # -1 --> auto arrage
print(arr.reshape(-1, 3))