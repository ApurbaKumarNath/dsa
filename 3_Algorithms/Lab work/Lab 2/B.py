def merge_sorted(n, m, arr1, arr2):
    i = 0
    j = 0
    temp = []
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            temp.append(arr1[i])
            i += 1
        else:
            temp.append(arr2[j])
            j += 1
    while i < n:
        temp.append(arr1[i])
        i += 1
    while j < m:
        temp.append(arr2[j])
        j += 1
    print(' '.join(map(str, temp)))

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

merge_sorted(n, m, arr1, arr2)