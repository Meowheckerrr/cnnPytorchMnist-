import os 

import torch 
import torch.nn as nn
import torch.nn.functional as F


import numpy as np 
import pickle 

import matplotlib.pyplot as plt

# os.environ['KMP_DUPLICATE_LIB_OK']='True'
train_data_dir = '../input/verification-data/train_data.bin'
val_data_dir = '../input/verification-data/val_data.bin'
verification_code_dir = '../input/verification-data/verification_code_data.bin'

def load_file(file_name):
    with open(file_name, mode='rb') as f:
        result = pickle.load(f)
    return result
# 查看所有类别的图片
train_data = load_file(train_data_dir)
img_test = list()
for i in range(1,1800,50):
    img_test.append(train_data[i][1])
plt.figure()
for i in range(1,37):
    plt.subplot(6,6,i)
    plt.imshow(img_test[i-1])
    plt.xticks([])
    plt.yticks([])
plt.show()