# indentity matrix 
import numpy as np

matrix = np.array([1,2,3,4]).reshape(2, 2)
print(matrix)

print("create identity matrix")

identityMatrix = np.eye(matrix.shape[0],dtype=int)  # 單位矩陣
print(identityMatrix)

vector = np.array([1,2])

result=np.dot(vector,vector) # vector 內積

print(result)

print("--------------------------------------------")

print("iXmatrix")
iXmatrix = np.dot(identityMatrix,matrix)
print(iXmatrix)

print(" matirx X matrix ")
matrixXmatrix= np.dot(matrix,matrix)
print(matrixXmatrix) #cauclate