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


## Question 3:
<table align="center", height="300">
  <td><img src = "https://github.com/user-attachments/assets/f70d744c-bd1a-4984-acd6-9211b813f54e"/></td>
</table>

## Solution:
<table align="center">
<td>
  
```py
def nTriangle(n:int) ->None:
    for i in range(1, n + 1):
        print(1, end = ' ')
        for j in range(2, i + 1):
            print(j, end = ' ')
        print()
```

</td>

<td>
  
```py
def nTriangle(n:int) ->None:
    i = 1
    while i <= n:
        print(1, end = ' ')
        j = 2
        while j <= i:
            print(j, end = ' ')
            j += 1
        print()
        i += 1
```

</td>

</table>

## Question 4:
<table align="center", height="300">
  <td><img src = "https://github.com/user-attachments/assets/8f198adf-f3fa-4d4d-b93b-3b2f494dcd58"/></td>
</table>

## Solution:
<table align="center">
<td>
  
```py
def triangle( n:int) ->None:
    for i in range(1, n + 1):
        print(i, end = ' ')
        for j in range(i-1):
            print(i, end = ' ')
        print()
```

</td>

</table>


## Question 5:
<table align="center", height="300">
  <td><img src = "https://github.com/user-attachments/assets/90f8ac0e-80b7-46de-9055-2205ce2f4b95"/></td>
</table>

## Solution:
<table align="center">
<td>
  
```py
# better approach: i represents lines (how many rows)     
# j represents content in the lines
def seeding(n: int) -> None:
    for i in range(1, n + 1):
        for j in range(n + 1 - i):
            print('*', end = ' ')
        print()
```

</td>

<td>
  
```py
# previous way:
def seeding(n: int) -> None:
    for i in range(n, 0, -1):
        print('*', end = ' ')
        for j in range(1, i):
            print('*', end = ' ')
        print()
```

</td>

</table>




## Question 6:
<table align="center", height="300">
  <td><img src = "https://github.com/user-attachments/assets/d859b084-0598-4b03-9dd5-ec4423cb03d7"/></td>
</table>

## Solution:
<table align="center">
<td>
  
```py

def nNumberTriangle(n: int) -> None:
    for lines in range(n):
        for content in range(1, n - lines + 1):
            print(content, end = ' ')
        print()
```

</td>
</table>

## Question 7:
<table align="center", height="300">
  <td><img src = "https://github.com/user-attachments/assets/7755cf00-1001-45ca-8983-cf3df966d2cd"/></td>
</table>

## Solution:
<table align="center">
<td>
  
```py

def nStarTriangle(n: int) -> None:
    overall_contents = n + n - 1
    '''
    e.g. 3 lines means (3+3-1) contents
    [space, star, space], so, if n = 3,
    [2, 1, 2]
    [1, 3, 1]
    [0, 5, 0]
    '''
    for lines in range(1, n + 1):

        space_needed = (overall_contents//lines)//2
        for space in range(space_needed):
            print(' ', end = '')
        
        for stars in range(lines + lines - 1):
            print('*', end = '')

        for space in range(space_needed):
            print(' ', end = '')
        print()
```

</td>

<td>
  
```py

'''
i represents lines
for n = 3 (i goes 1 to 3 => lines)

for 1st line, n - i = 3 - 1 = 2 spaces (adding at left)
similarly, 2nd line = 1 space (adding at left)
so, did the same adding for right side in this code

and for the stars,
1st line, 2*i - 1 = 1 star
similarly, 2nd line, 3 stars and so on
'''
def nStarTriangle(n: int) -> None:
    for i in range(1, n + 1):
        for space in range(1, n - i + 1):
            print(' ', end = '')
        for star in range(1, 2*i):
            print('*', end = '')
        for space in range(1, n - i + 1):
            print(' ', end = '')
        print()
```

</td>
</table>

## Question 8:
<table align="center", height="300">
  <td><img src = "https://github.com/user-attachments/assets/066c3776-7a78-457b-93e8-f06327e7c05c"/></td>
</table>

## Solution:
<table align="center">
<td>
  
```py

def nStarTriangle(n: int) -> None:
    for lines in range(n, -1, -1):
        for space in range(n - lines):
            print(' ', end = '')
        connection = 1
        for star in range(2*lines - 1):
            print('*', end = '')
        for space in range(n - lines):
            print(' ', end = '')
        connection = 1
        print()
```

</td>
</table>

## Question 9:
<table align="center", height="300">
  <td><img src = "https://github.com/user-attachments/assets/dc0802f0-42df-4c59-86ce-6d4324ea8feb"/></td>
</table>

## Solution:
<table align="center">
<td>
  
```py

def nStarDiamond(n: int) -> None:
    for lines in range(n):
        SameLines(lines, n)
    for lines in range(n - 1, -1, -1):
        SameLines(lines, n)

def SameLines(lines, n):
    for space in range(n - lines - 1):
        print(' ', end = '')
    for star in range(2*lines + 1):
        print('*', end = '')
    for space in range(n - lines - 1):
        print(' ', end = '')
    print()
```

</td>
</table>

## Question 10:
<table align="center", height="300">
  <td><img src = "https://github.com/user-attachments/assets/8cc4232e-9c7d-41bd-9385-d89928639cdd"/></td>
</table>

## Solution:
<table align="center">
<td>
  
```py

def nStarTriangle(n: int) -> None:      
    for line in range(1, n + 1):
        SameLines(line)
    for line in range(n - 1, 0, -1):
        SameLines(line)
        
def SameLines(line):
    for star in range(line):
        print('*', end = '')
    print()
```

</td>
</table>

## Question 11:
<table align="center", height="300">
  <td><img src = "https://github.com/user-attachments/assets/dac0d4a7-9bb4-4258-8cf3-d7eb4b3de7f0"/></td>
</table>

## Solution:
<table align="center">
<td>
  
```py

def nBinaryTriangle(n: int) -> None:
    for line in range(1, n + 1):
        if line % 2 != 0:
            for binary in range(1, line + 1):
                print(binary % 2, end = ' ')
        else:
            for binary in range(0, line):
                print(binary % 2, end = ' ')
        print()
```

</td>
</table>

## Question 12:
<table align="center", height="300">
  <td><img src = "https://github.com/user-attachments/assets/bf4ee73b-7415-42ec-9c42-48e027405b77"/></td>
</table>

## Solution:
<table align="center">
<td>
  
```py

def numberCrown(n: int) -> None:
    for line in range(1, n + 1):
        for num in range(1, line + 1):
            print(num, end = ' ')
        for space in range(4*(n - line)):
            print(' ', end = '')
        for num in range(line, 0, -1):
            print(num, end = ' ')
        print()
```

</td>
</table>

## Question 13:
<table align="center", height="300">
  <td><img src = "https://github.com/user-attachments/assets/39783e5d-d227-4251-91a6-3e381cfebf0d"/></td>
</table>

## Solution:
<table align="center">
<td>
  
```py

def nNumberTriangle(n: int) -> None:      
    tracker = 1
    for line in range(1, n + 1):
        for num in range(1, line + 1):
            print(tracker, end = ' ')
            tracker += 1
        print()
```

</td>
</table>

## Question 14:
<table align="center", height="300">
  <td><img src = "https://github.com/user-attachments/assets/606366ce-3a2d-4f08-a7e8-c8a33a2cd6f4"/></td>
</table>

## Solution:
<table align="center">
<td>
  
```py

def nLetterTriangle(n: int) -> None:    
    for lines in range(1, n + 1):
        char = 65
        for letter in range(lines):
            print(chr(char + letter), end = ' ')
        print()
```

</td>
</table>

## Question 15:
<table align="center", height="300">
  <td><img src = "https://github.com/user-attachments/assets/cb429d7a-6283-4d71-b1a2-9e237226e7e7"/></td>
</table>

## Solution:
<table align="center">
<td>
  
```py

def nLetterTriangle(n: int):
    for lines in range(n, 0, -1):
        char = 65
        for letter in range(lines):
            print(chr(char + letter), end = ' ')
        print()
```

</td>
</table>

## Question 16:
<table align="center", height="300">
  <td><img src = "https://github.com/user-attachments/assets/dba8e47b-9bb4-48e7-8226-6ecd3e46d98b"/></td>
</table>

## Solution:
<table align="center">
<td>
  
```py

def alphaRamp(n: int) -> None:
    char = 65
    for lines in range(1, n + 1):
        for letter in range(lines):
            print(chr(char), end = ' ')
        char += 1
        print()
```

</td>
</table>

## Question 17:
<table align="center", height="300">
  <td><img src = "https://github.com/user-attachments/assets/a3c0cf24-c4c1-42f8-b082-5151a65bbf8e"/></td>
</table>

## Solution:
<table align="center">
<td>
  
```py

def alphaHill(n: int):
    for line in range(1, n + 1):
        char = 65
        for space in range(2*(n - line)):
            print(' ', end = '')
        for letter in range((2*line - 1)//2 + 1):
            print(chr(char + letter), end = ' ')
        for letter in range((2*line - 1)//2 - 1, -1, -1):
            print(chr(char + letter), end = ' ')
        for space in range(2*(n - line)):
            print(' ', end = '')
        print()
```

</td>
</table>

## Question 18:
<table align="center", height="300">
  <td><img src = "https://github.com/user-attachments/assets/7dbc10c4-cd19-40fa-a80f-0d01b6a388c6"/></td>
</table>

## Solution:
<table align="center">
<td>
  
```py

def alphaTriangle(n: int):
    for lines in range(1, n + 1):
        char = 65 + (n - 1)
        for letter in range(lines):
            print(chr(char - letter), end = ' ')
        print()
```

</td>
</table>

## Question 19:
<table align="center", height="300">
  <td><img src = "https://github.com/user-attachments/assets/43fc9c91-03ad-4fea-a069-c0fe0ed98582"/></td>
</table>

## Solution:
<table align="center">
<td>
  
```py

def symmetry(n: int):
    for line in range(1, n + 1):
        SameLines(line, n)
    for line in range(n, 0, -1):
        SameLines(line, n)
        

def SameLines(line, n):
    for star in range(n - line + 1):
        print('*', end = ' ')
    for space in range(4*(line - 1)):
        print(' ', end = '')
    for star in range(n - line + 1):
        print('*', end = ' ')
    print()
```

</td>
</table>

## Question 20:
<table align="center", height="300">
  <td><img src = "https://github.com/user-attachments/assets/11f483b1-eba2-4685-9989-350f14e0da6e"/></td>
</table>

## Solution:
<table align="center">
<td>
  
```py

'''
for n = 3, 
line = 1, star = 1, space = 8, star = 1
line = 2, star = 2, space = 4, star = 2
line = 3, star = 3, space = 0, star = 3

here, line == star

and, overall content in a line,
n*4 = [spaces_with_stars + (star + star) + spaces]
3*4 = [4 + (2 + 2) + 4] for line = 2
so, spaces = 4*n - 2*star - spaces_with_stars
    spaces = 4(n - line) {as line = 2*star + spaces_with_stars}
'''

def symmetry(n: int):
    for line in range(1, n + 1):
        SameLines(line, n)
    for line in range(n - 1, 0, -1):
        SameLines(line, n)
        
def SameLines(line, n):
    for star in range(1, line + 1):
        print('*', end = ' ')
    for space in range(4*(n - line)):
        print(' ', end = '')
    for star in range(1, line + 1):
        print('*', end = ' ')
    print()
        
```

</td>
</table>

## Question 21:
<table align="center", height="300">
  <td><img src = "https://github.com/user-attachments/assets/89507d2d-074b-4ab1-b59a-e5067363ebe6"/></td>
</table>

## Solution:
<table align="center">
<td>
  
```py

def getStarPattern(n: int) -> None:
    for line in range(1, n + 1):
        if line == 1 or line == n:
            for star in range(n):
                print('*', end = '')

        else:
            print('*', end = '')
            for space in range(n - 2):
                print(' ', end = '')
            print('*', end = '')
        print()
```

</td>
</table>

## Question 22:
<table align="center", height="300">
  <td><img src = "https://github.com/user-attachments/assets/1bf9af6c-5b06-4230-803e-cd78daab53a8"/></td>
</table>

## Solution:
<table align="center">
<td>
  
```py
# this solution is wrong for numbers greater than 9
# it was hard for me to come up with this solution without taking any help
# that's why I'm not removing it
def getNumberPattern(n: int) -> None:
    save = ''
    full_save = []
    for line in range(1, n + 1):
        for num in range(1, n + 1):
            if num == line:
                changed_num = f'{n - line + 1}'
                save += changed_num
                all_save = save
            elif num > line:
                all_save += changed_num
        remaining = ''
        for reverse in range(-2, -len(all_save)-1, -1):
            remaining += all_save[reverse]
        full_save.append(all_save + remaining)
    temp = list(full_save)
    for full_reverse in range(-2, -len(full_save)-1, -1):
        full_save.append(temp[full_reverse])
    for num in full_save:
        print((num))
```

</td>

<td>
  
```py

def getNumberPattern(n: int) -> None:
    for i in range(2*n - 1):
        for j in range(2*n - 1):
            top = i
            left = j
            right = 2*(n-1) - j
            down = 2*(n-1) - i
            print(n - min(min(top, down), min(left, right)), end = '')
        print()
```

</td>
</table>
