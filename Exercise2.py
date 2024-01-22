import numpy as np

#2a
a = np.array([5, 4, 9, 2, 0, 4, 7, 2])
print(a[-1])

#2b
print(a[1:6])
print(a[:-2])
print(a[::2])

#2c

a[-1] = -9
print(a)
a[0:3]= 1
print(a)
print("")
#3a

A = np.array([[1, 0, 0, 0 ],[1, -2, 1, 0 ],[0, 1, -2, 1], [0, 0, 0, 1]])
b = np.array([0, 1, 1, 2])
x = np.linalg.solve(A, b)
print(x)

result = np.dot(A, x) - b
print(result)

