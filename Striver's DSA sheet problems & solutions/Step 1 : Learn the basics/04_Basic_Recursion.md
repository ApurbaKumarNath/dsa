## Question 1:
<table align="center", height="300">
  <td width = 600><img src = "https://github.com/user-attachments/assets/39dfef10-b685-488b-b8d5-a0f5d4b92834"/></td>
</table>

## Solution:
<table align="center">
<td>

```py
# Using Backtrack
class Solution:
        
    def printNos(self,N):
        if(N>0):
            self.printNos(N-1)
            print(N,end=" ")
```
 </td>
 
 <td>
   
```py
# Using Backtrack
''' A concept to understand:
  changing i in function changes things.
  e.g. f(i) turns to f(changed_i)
'''
class Solution:
        
    def printNos(self, i, N):
        if i == 1:
            return None
        else:
            i -= 1 # this line turns printNos(4, 3) into printNos(3, 3) and so on
            self.printNos(i, N)
            print(i, end = ' ')

            
f = Solution()
f.printNos(4, 3)
```
</td>

<td>
  
```py
# Using Backtrack
class Solution:
        
    def printNos(self, i, N):
        if i > 0:
            self.printNos(i - 1, N)
            print(i, end = ' ')

        else:
            return None
```
</td>

<td>

  
```py
# Without Backtrack
class Solution:
        
    def printNos(self, i, N):
        if i <= N:
            print(i, end = ' ')
            self.printNos(i + 1, N)

            
f = Solution()
f.printNos(1, 3)
```
</td>

</table>

## Question 2:
<table align="center", height="300">
  <td width = 600><img src = "https://github.com/user-attachments/assets/ccb6413d-7738-48ec-ba75-237aa419f90f"/></td>
</table>

## Solution:
<table align="center">
<td>

```py
# Using Backtrack
class Solution:
    def printNos(self, n):
        if n > 0:
            print(n, end = ' ')
            self.printNos(n - 1)
```
</td>

<td>

```py
# Without Backtrack
class Solution:
    def printNos(self, n):
        if n == 0:
            return None
        else:
            print(n, end = ' ')
            self.printNos(n - 1)
```
</td>

</table>

## Question 3:
<table align="center", height="300">
  <td width = 600><img src = "https://github.com/user-attachments/assets/12504dcd-66ce-4886-a238-3ab025ef4fd9"/></td>
</table>

## Solution:
<table align="center">
<td>

```py
# Without backtrack
class Solution:
    def sumOfSeries(self, n, summ = 0):
        if n < 0:
            print(summ)
        else:
            self.sumOfSeries(n - 1, summ + n**3)
```
</td>

<td>

```py
# Using backtrack
class Solution:
    def sumOfSeries(self, n):
        if n == 0:
            return n**3
        else:
            return (self.sumOfSeries(n - 1) + n**3)
            #print(self.sumOfSeries(n - 1) + n**3) # can't print int + Nonetype
```
</td>

<td>

```py
#using formula to calculate the sum of series     
class Solution:
    def sumOfSeries(self,n):
        ans=(n*(n+1))**2//4
        return ans
```
</td>

</table>

## Question 4:
<table align="center">
  <td><pre>Factorial of N numbers</pre></td>
</table>

## Solution:
<table align="center">
<td>

```py
# Using recursion
class Solution:
    def factorialNumbers(self, n):
    	if n == 1:
    	    return 1
    	else:
    	    return (n * self.factorialNumbers(n - 1))
            
f = Solution()
print(f.factorialNumbers(3)) # Output: 6
```
</td>

</table>

## Question 5:
<table align="center">
  <td><pre>Reverse an array</pre></td>
</table>

## Solution:
<table align="center">
<td>

```py
# Using recursion
def reversing(i, li, n):
    if i >= n:
        return None
    li[i], li[n] = li[n], li[i]
    reversing(i + 1, li, n - 1)
    
li = [1, 2, 3, 4, 'kk']
reversing(0, li, len(li) - 1)
print(li)
```
</td>

</table>

## Question 6:
<table align="center">
  <td><pre>Check if a string is palindrome or not</pre></td>
</table>

## Solution:
<table align="center">
<td>

```py
# Using recursion
def reversing(arr, i = 0):
    if i == len(arr)//2:
        return True
    elif arr[i] != arr[len(arr) - i - 1]:
        return False
    else:
        return reversing(arr, i + 1)
        ''' Here, the value of the function will return as True or False
            But if you only call the funciton, None will be returned to the
            first fuction that was called in the print() function.'''
    
arr = 'MADAM'
print(reversing(arr))
```
</td>

</table>

## Question 7:
<table align="center">
  <td><pre>Fibonacci Number</pre></td>
</table>

## Solution:
<table align="center">
<td>

```py
# Using recursion
def fibonacci(n): # n = nth fibonacci number
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(4)) # 4th fibonacci number = 3
```
</td>

</table>
