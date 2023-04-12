import numpy as np 

A = np.array([1, 2, 3, 4]).reshape(2, 2)
B = np.array([5, 6, 7, 8]).reshape(2, 2)


Ainverse = np.linalg.inv(A)

X = np.dot(Ainverse,B)

print(X)