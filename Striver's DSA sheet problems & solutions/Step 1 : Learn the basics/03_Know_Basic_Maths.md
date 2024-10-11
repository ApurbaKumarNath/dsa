## Question 1:
<table align="center", height="300">
  <td width = "700"><img src = "https://github.com/user-attachments/assets/4fa0243c-c904-4cf8-a204-49d55c0b26e7"/></td>
</table>

## Solution:
<table align="center">
<td>
  
```py
class Solution:
    def evenlyDivides (self, N):
        num = N
        count = 0
        while N > 0:
            last = N % 10
            if last != 0 and num % last == 0:
                count += 1
            N = int(N/10) # N//10 also works
        return count
```

</td>

</table>


## Question 2:
<table align="center", height="300">
  <td><img src = "https://github.com/user-attachments/assets/f82dc3d4-f8c0-4b04-9749-5ba7293bd254"/></td>
</table>

## Solution:
<table align="center">
<td>
  
```py
class Solution:
    def reverse(self, x: int) -> int:
        int_min, int_max = (-2)**31, (2**31) - 1
        if x > int_max or int_min > x:
            return 0
        else:
            track = 1
            if x < 0:
                track = -1
                x = x*(track)
            divisor = self.divider(x)
            mul = 1
            prev = 0
            while divisor > 0:
                last = ((x // divisor) * mul) + prev
                x = x % divisor
                divisor = divisor//10
                prev = last
                mul *= 10
            result = last*track
            if result > int_max or int_min > result:
                return 0
            else:
                return result

    def divider(self, y):
        div = 1
        while y // 10 > 0:
            div *= 10
            y = y // 10
        return div
```

</td>

<td>
  
```py
class Solution:
    def reverse(self, x: int) -> int:
        # Limits for a 32-bit signed integer
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Initialize the result variable
        result = 0
        
        # Handle the sign of the input number
        if x < 0:
            sign = -1  
        else: 
            sign = 1
        x *= sign
        
        # Reverse the integer
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check overflow before updating result
            #if (result > (INT_MAX - digit) // 10):
                #return 0
            
            result = result * 10 + digit
            if result > INT_MAX:
                return 0
        
        return sign * result
```

</td>

</table>

## Question 3:
<table align="center", height="300">
  <td width = "900"><img src = "https://github.com/user-attachments/assets/d24861ec-0603-49e7-a545-39cff34cf984"/></td>
</table>

## Solution:
<table align="center">
<td>
  
```py
class Solution:
    def isPalindrome(self, x: int) -> bool:     
        if 0 <= x <= 9:
            return True
        if x < 0 or (x % 10 == 0):
            return False
        else:
            copy = x
            rev = 0
            while x > 0:
                last_digit = x % 10 
                rev = rev*10 + last_digit
                if rev > (2**31) - 1:
                    return False
                x //= 10
            if rev == copy:
                return True
            else:
                return False

```

</td>

</table>

## Question 4:
<table align="center">
  <td>
    <pre>
      Armstrong Number 
      problem example: 371 = 3&sup3 + 7&sup3 + 1&sup3 => True
      Example: 1634 = 1<sup>4</sup> + 6<sup>4</sup> + 3<sup>4</sup> + 4<sup>4</sup> => True
    </pre>
  </td>
</table>

## Solution:
<table align="center">
<td>
  
```py
num = int(input())
count = 0
copy1 = num
copy2 = num
while num > 0:
    num //= 10
    count += 1
armstrong = 0
while copy1 > 0:
    armstrong += (copy1 % 10)**count
    copy1 //= 10
if armstrong == copy2:
    print(True)
else:
    print(False)

```

</td>

</table>


## Question 5:
<table align="center", height="400">
  <td><img src = "https://github.com/user-attachments/assets/2b4a48b5-9269-4dd7-802f-a95e9903deb1"/></td>
  <td><img src = "https://github.com/user-attachments/assets/4cccd21b-285d-49ea-9fcc-7de32e851f4c"/></td>
</table>

## Solution:
<table align="center">
<td>
  
```py
# from 1 to sqrt(num) => divisors and (num / divisors) == all divisors         
# Another idea ==> for finding prime numbers, loop till sqrt(N) 
class Solution:
    def sumOfDivisors(self, N):
        if 1 <= N < 10**6:
            out = 0
        	for i in range(1, N + 1):
        	    summ = 0
        	    for x in range(1, int(i**0.5) + 1):
                    if i % x == 0 and i/x != float(x):
                        summ = summ + x + (i//x)
                    elif i/x == float(x):
                        summ += x
                out += summ
        	return out
        else:
            return 0
```

</td>

<td>
  
```py
class Solution:
    def sumOfDivisors(self, N):
        sum = 0

        # Iterating from 1 to N.
        for i in range(1, N + 1):
            # Calculating and accumulating the sum of divisors.
            sum += (N // i) * i

        # Returning the sum of divisors.
        return sum
```

</td>

</table>


## Question 6:
<table align="center">
  <td>
  <pre>
    Finding GCD/HCF:
    *euclidean algorithm*
    for numbers N1, N2:
      gcd (N1, N2) = gcd (N1 - N2, N2) [if N1 > N2]
      e.g. gcd(6, 2) = gcd(4, 2) = gcd(2, 0) 
      when one is zero, the other is gcd. here ==> 2
    Faster approach example:
      gcd(52, 10) --> 52 % 10 --> gcd(2, 10) -->
      10 % 2 --> gcd(0, 2) ==> gcd = 2
  </pre>
  </td>
</table>

## Solution:
<table align="center">
<td>
  
```py
a, b = int(input()), int(input())      
while a > 0 and b > 0:
    if a >= b:
        a = a % b
    else:
        b = b % a
    if a == 0:
        gcd = b
    else:
        gcd = a
print(gcd)

```

</td>

</table>
