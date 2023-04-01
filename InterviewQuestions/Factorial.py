def Factorial(n): 
    if n == 1: 
        return n 
    return n * Factorial(n-1)




f = Factorial(4)
print(f)