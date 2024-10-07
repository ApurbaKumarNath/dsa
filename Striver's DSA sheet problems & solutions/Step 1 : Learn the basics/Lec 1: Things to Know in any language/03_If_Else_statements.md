## Question:
<table align="center", height="400">
  <td><img src = "https://github.com/user-attachments/assets/ad039f2e-896e-4230-8852-f04b58ca8fa3"/></td>
  <td><img src = "https://github.com/user-attachments/assets/22eb024a-4cd5-485f-8e6b-f7ee47eff843"/></td>
</table>

## Solution:
```py
''' Newly learned:
data types can be set when defining the function like: def f(n : int, m : int) -> str
'''
```

```py
class Solution:
    def compareNM(self, n : int, m : int) -> str:
        if n < m:
            return 'lesser'
        elif n == m:
            return 'equal'
        else:
            return 'greater'
```
