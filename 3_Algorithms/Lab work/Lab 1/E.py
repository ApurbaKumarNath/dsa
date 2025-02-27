def bubbleSort(arr):                                                    
    for i in range(len(arr)-1):
        swapped= False
        for j in range(len(arr)-i-1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    
    return arr

N = int(input())

numbers = input().split()
if len(numbers) == N:
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])

    sorted_arr = bubbleSort(numbers)
    for i in range(len(sorted_arr)):
        print(sorted_arr[i], end=' ')