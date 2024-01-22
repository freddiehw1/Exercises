import numpy as np
#3a
A = np.array([[1, 0, 0, 0 ],[1, -2, 1, 0 ],[0, 1, -2, 1], [0, 0, 0, 1]])
b = np.array([0, 1, 1, 2])
x = np.linalg.solve(A, b)
print(x)

result = np.dot(A, x) - b
print(result)

