import numpy as np


matrix = np.arange(6).reshape(2,3)

print(matrix)


print("transport")
print(np.transpose(matrix))
print(matrix.T)