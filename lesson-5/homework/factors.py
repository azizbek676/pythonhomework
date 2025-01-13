def find_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:  
            factors.append(i)
    
    return factors
n = int(input("Enter a positive integer: "))  
factors = find_factors(n)
print(f"The factors of {n} are: {factors}")
