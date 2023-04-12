
import numpy as np 
arr = np.arange(1, 4)

print(arr.reshape(-1, 1)) # 重塑成二維的欄
print(arr.reshape(1, -1)) # 重塑成二維的列