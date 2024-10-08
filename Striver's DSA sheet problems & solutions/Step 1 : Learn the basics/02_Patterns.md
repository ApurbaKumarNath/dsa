## Question 1:
<table align="center", height="400">
  <td width = "400"><img src = "https://github.com/user-attachments/assets/a69fed1f-d7de-448f-948d-8835c01e8417"/></td>
</table>

## Solution:
<table align="center">
<td>
  
```py
def nForest(n:int) ->None:
    i = 0
    while i < n:
        print('* ', end = '')
        j = 1
        while j < n:
            print('* ', end = '')
            j += 1
        print()
        i += 1
```

</td>

<td>
  
```py
def nForest(n:int) ->None:
    i = 1
    while i <= n:
        print('* ', end = '')
        j = 1
        while j <= n - 1:
            print('* ', end = '')
            j += 1
        print()
        i += 1
```

</td>

<td>
  
```py
# Shortcut solution
# (not preferred)

def nForest(n:int) ->None:
    i = 1
    while i <= n:
        print(n*'* ')
        i += 1
```

</td>
</table>


## Question 2:
<table align="center", height="300">
  <td width = "450"><img src = "https://github.com/user-attachments/assets/c16e39f4-6450-43b5-88f4-80e718732de9"/></td>
</table>

## Solution:
<table align="center">

<td>
  
```py
def nForest(n:int) ->None:
    for i in range (n):
        print('* ', end = '')
        for j in range(i):
            print('* ', end = '')
        print()
```

</td>

<td>
  
```py
def nForest(n:int) ->None:
    i = 1
    while i <= n:
        print('* ', end = '')
        j = 1
        while j <= i - 1:
            print('* ', end = '')
            j += 1
        print()
        i += 1
```

</td>

</table>
