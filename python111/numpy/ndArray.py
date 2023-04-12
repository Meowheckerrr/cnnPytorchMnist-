import numpy as np
import matplotlib.pyplot as plt

#ndarray 在同質數值陣列計算的便利性相較原生 list 具有絕對的優勢
#一是使用 np.array() 將既有的 list 轉換成為 ndarray


homogeneous_list = [1, 2, 3, 4, 5]  #原生python 
print(type(homogeneous_list))

arr = np.array(homogeneous_list)   
print(type(arr))
print(arr)
print(arr.dtype)


# np.array() 可以搭配 dtype 參數指定資料型態，可以傳入下列常見的資料型態：


arr = np.array(homogeneous_list, dtype=float)
arr.dtype

# 等差、均勻間隔的數列，則可以使用下列函式

np.arange(1, 10, 2) # 1,3,5,7,9

np.linspace(1, 9, 5, dtype=int)
