import numpy as np
import matplotlib.pyplot as plt


# scalar 

scalar = np.array(5566)
print(scalar)
print(scalar.ndim) #dimension
print(scalar.shape) #dimension ixj

print("---------------------------------")

# matrix 

matrix = np.array([5, 5, 6, 6]).reshape(2, 2)
print(matrix)
print(matrix.ndim)  # dimension 
print(matrix.shape)  #ixj

print("----------------------------------------------")

# tensor 
tensor = np.array([5, 5, 6, 6]*3).reshape(3, 2, 2)
print(tensor)
print(tensor.ndim)
print(tensor.shape)