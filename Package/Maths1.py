def SQRT(n):
    return n **0.5

def POWER(a,b):
    return a**b

def FACTORIAL(n): 
    result = 1 
    for i in range(1, n + 1): 
        result *= i 
    return result

def Even_Odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

def Prime(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1

    if count > 2:
        return "Not a Prime Number"
    else:
        return "Prime Number"