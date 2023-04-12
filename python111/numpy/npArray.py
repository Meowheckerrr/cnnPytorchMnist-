import numpy as np
import matplotlib.pyplot as plt


heterogeneous_list = [5566, 55.66, True, False, '5566'] #異構 Data 
for i in heterogeneous_list:
    print(type(i)) #list 中每個元素都是一個完整的 Python 物件


array = np.array([1,2,3,4,5])



print(array ** 2)