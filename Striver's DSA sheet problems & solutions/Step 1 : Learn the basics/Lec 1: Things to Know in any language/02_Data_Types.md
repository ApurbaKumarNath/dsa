## Question:
<table align="center", height="400">
  <td><img src = "https://github.com/user-attachments/assets/5ebf2f60-4a48-44b8-a67c-ab69aaea47a6"/></td>
  <td><img src = "https://github.com/user-attachments/assets/ab6ea746-b106-4782-afee-8c8e2e49ce12"/></td>
</table>

## Solution:
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
