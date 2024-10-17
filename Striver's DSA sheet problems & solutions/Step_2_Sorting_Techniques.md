## Question 1:
<table align="center">
  <td><pre>Selection Sort</pre></td>
</table>

## Solution:
<table align="center">
<td>

```py
# Select the minimum and swap
def selection_sort(arr):
    for num in range(len(arr) - 1):
        minn = num
        for check in range(num + 1, len(arr)):
            if arr[check] < arr[minn]:
                minn = check
        arr[num], arr[minn] = arr[minn], arr[num]
    return arr
arr = [2, 3, 2, 5, 1, 1, 5]
print(selection_sort(arr))
```
</td>

</table>
