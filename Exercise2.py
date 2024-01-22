import numpy as np

#2a
a = np.array([5, 4, 9, 2, 0, 4, 7, 2])
print(a[-1])

#2b
print(a[1:6])
print(a[:-2])
print(a[::2])

a[-1] = -9
print(a)
a[0:3]= 1
print(a)

#2c
