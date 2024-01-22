import numpy as np 
import matplotlib.pyplot as plt 


#4a

t = np.linspace(0,5, 500)
y = t**2 * np.exp(-2 * t)

#4b
plt.plot(t,y, color = 'r', linewidth = '1')
plt.xlabel("t")
plt.ylabel("y")
plt.show()

#4c 
print(np.max(y))

#4d
max_t_index = np.argmax(y)
t_at_max_y = t[max_t_index]
print(t_at_max_y)





