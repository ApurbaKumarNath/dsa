def power_mod(a, b, mod = 107): # binary exponentiation

    result = 1
    a = a % mod  # Reduce a initially to avoid overflow
    
    while b > 0:
        # If b is odd, multiply result with a
        if b % 2 == 1:
            result = (result * a) % mod
        
        # Square a and halve b
        a = (a * a) % mod
        b //= 2
    
    return result

a, b = map(int, input().split())

result = power_mod(a, b)

print(result)