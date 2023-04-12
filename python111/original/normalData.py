

import numpy as np 
import matplotlib.pyplot as plt

arr = np.random.normal(size=10000) #10000 常態分布數據

fig = plt.figure() #直方圖
ax = plt.axes() # 創建一個子圖對象
ax.hist(arr, bins=50)  #數據劃分為 50 個區間，計算每個區間中數據的頻率
plt.show()