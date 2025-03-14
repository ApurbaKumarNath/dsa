def merge(a, b):
    temp = []
    i = 0
    j = 0
    count = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            temp.append(a[i])
            i += 1
        else:
            temp.append(b[j])
            j += 1
            count += len(a) - i # count inversions

    while i < len(a):
        temp.append(a[i])
        i += 1
    
    while j < len(b):
        temp.append(b[j])
        j += 1
    
    return count, temp


def mergeSort(arr):
    if len(arr) <= 1:
        return 0, arr
    else:
        mid = len(arr)//2
        c1, a1 = mergeSort(arr[0 : mid])
        c2, a2 = mergeSort(arr[mid : len(arr)])
        count, arr2 = merge(a1, a2) 
        return c1 + c2 + count, arr2
    

n = int(input())
arr = list(map(int, input().split()))
inversion, ans = mergeSort(arr)
print(inversion)
for i in ans:
    print(i, end = ' ')