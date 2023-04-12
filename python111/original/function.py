import numpy as np 
import matplotlib.pyplot as plt

# 定義 epsilon，避免 log 函式輸入為 0 時產生無限大
eps = 1e-06

# 生成 10000 個介於 0 + eps 到 1 - eps 之間的數字
p = np.linspace(0 + eps, 1 - eps, 10000)

# 計算 y_true 為 0 或 1 時的對數損失值
log_loss_0 = -np.log(1-p)
log_loss_1 = -np.log(p)

# 印出 p、log_loss_0 和 log_loss_1 的值
print(p) 
print(log_loss_0)
print(log_loss_1)

# 繪製兩條線，分別代表 y_true 為 0 或 1 時的對數損失值
fig = plt.figure()
ax = plt.axes()
ax.plot(p, log_loss_0, label='$y_{true}=0$')
ax.plot(p, log_loss_1, label='$y_{true}=1$')

# 添加圖例，顯示 y_true 為 0 或 1 時的含義
ax.legend()

# 顯示繪製好的圖形
plt.show()