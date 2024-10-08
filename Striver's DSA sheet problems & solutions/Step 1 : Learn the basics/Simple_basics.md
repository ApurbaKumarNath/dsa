## Question:
<table align="center", height="400">
  <td><img src = "https://github.com/user-attachments/assets/5ebf2f60-4a48-44b8-a67c-ab69aaea47a6"/></td>
  <td><img src = "https://github.com/user-attachments/assets/ab6ea746-b106-4782-afee-8c8e2e49ce12"/></td>
</table>

## Solution:
```py
''' hint:
Byte size: str = 1, int & float = 4, long & double = 8
also check online as 32-bit and 64 bit matters
'''
```

```py
class Solution:
    def dataTypeSize(self, str):
        if str == 'Character':
            return 1
        if str == 'Integer' or str == 'Float':
            return 4
        if str == 'Long'  or str == 'Double':
            return 8
        else:
            return -1
```

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
