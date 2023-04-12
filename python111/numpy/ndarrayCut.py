# Array  取出 data 

import numpy as np

array = np.arange(10,20)

print(array[::])   #array[start:stop:step ]
print(array[::2])
print(array[:5])   # stop=5, 不包含
print(array[5:])   # start=5, 包含
print(array[::-1]) # step=-1, 反轉