def fast_mod(a, n, m):
    if a == 1:
        return n % m
    else:
        a_minus_1 = a - 1
        mod_val_abs = abs(m * a_minus_1)
        exponent = n + 1
        a_pow = pow(a, exponent, mod_val_abs)
        numerator = (a_pow - a) % mod_val_abs
        sum_mod = (numerator // a_minus_1) % m
        return sum_mod

T = int(input())
for i in range(T):
    a, n, m = map(int, input().split())
    print(fast_mod(a, n, m))