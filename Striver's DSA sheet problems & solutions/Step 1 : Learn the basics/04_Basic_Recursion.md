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
