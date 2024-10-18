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


## Question 2:
<table align="center">
  <td><pre>Bubble Sort</pre></td>
</table>

## Solution:
<table align="center">
<td>

```py
# Push the max to the last by adjacent swaps
def bubble_sort(arr):
    for num in range(len(arr)):
        for check in range(len(arr) - num - 1):
            if arr[check] > arr[check + 1]:
                arr[check], arr[check + 1] = arr[check + 1], arr[check]
                
arr = [1, 0, 4, 3, 0]
bubble_sort(arr)
print(arr)
```
</td>

</table>


## Question 3:
<table align="center">
  <td><pre>Inserstion Sort</pre></td>
</table>

## Solution:
<table align="center">
<td>

```py
# Take one element at a time and place it in its rightful position      
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
   
arr = [5, 0]
insertion_sort(arr)
print(arr)
```
</td>

</table>


## Question 4:
<table align="center">
  <td><pre>Merge Sort</pre></td>
</table>

## Solution:
<table align="center">
<td>

```py
# Divide and Merge   
def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    #looping [low to mid] and [mid+1 to high]
    while left <= mid and right <= high:
        # adding smaller number to temp
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    
    # if remains, add all to temp
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1
    
    for i in range(low, high + 1):
        arr[i] = temp[i - low]
    
    
# The dividing part:
def merge_sort(arr, low = 0, high = None):
    # wrong -> merge_sort(..., high = len(arr) - 1)
    if high == None: # the first high = None to avoid error
        high = len(arr) - 1
    if low == high:
        return
    else:
        #mid for dividing
        mid = (low + high)//2
        # left half
        merge_sort(arr, low, mid)
        # right half
        merge_sort(arr, mid + 1, high)
        # start merging
        merge(arr, low, mid, high)
   
arr = [5, 0, 4, 3, 2, 1]
merge_sort(arr)
print(arr)
```
</td>

</table>
