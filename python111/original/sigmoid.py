
import numpy as np 
import matplotlib.pyplot as plt


x = np.linspace(-6, 6, 1000)  # array 0~10000 element x -6~6

# 計算 Sigmoid 函數的值並存在陣列 fx 中
fx = 1 / (1 + np.exp(-x))

# 建立一個圖形物件
fig = plt.figure()

# 建立一個子圖形
ax = plt.axes()

# 畫出 x 與 fx 的圖形
ax.plot(x, fx)

# 顯示圖形
plt.show()