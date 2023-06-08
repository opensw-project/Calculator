import numpy as np

A = np.array([[2, 3], [5, 6]])
B = np.array([4, 5])

C = np.linalg.solve(A, B)

print(C)
 
