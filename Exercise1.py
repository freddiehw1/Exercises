from math import pi

#1a
def leibniz_approximation(N):
    pi_approximation = 0
    for n in range(N+1):
        pi_approximation += (8)/((4*n + 1)*(4*n+3))
    return pi_approximation

print(leibniz_approximation(100))
print(leibniz_approximation(1000))
print(leibniz_approximation(10000))
    
# 1b
def leibniz_error(approximation):
    error = abs(pi - approximation)
    return error 

print(leibniz_error(leibniz_approximation(100)))
print(leibniz_error(leibniz_approximation(1000)))
print(leibniz_error(leibniz_approximation(10000)))

    
    
    

    