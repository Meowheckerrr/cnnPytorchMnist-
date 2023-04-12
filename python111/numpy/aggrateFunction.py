import numpy as np

mat = np.arange(1, 16).reshape(3, 5)
print(np.sum(mat))         # 1 個輸出
print(np.sum(mat, axis=0)) # 5 個輸出
print(np.sum(mat, axis=1)) # 3 個輸出