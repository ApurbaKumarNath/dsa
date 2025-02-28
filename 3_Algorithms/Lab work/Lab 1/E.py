def bubbleSort(arr):                                                    
    for i in range(len(arr)-1):
        swapped= False
        for j in range(len(arr)-i-1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    
    print(' '.join(map(str, arr)))
    
N = int(input())

numbers = list(map(int, input().split()))
if len(numbers) == N:
    bubbleSort(numbers)