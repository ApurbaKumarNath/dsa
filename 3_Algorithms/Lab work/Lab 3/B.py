def find_max_combination(arr, start, end):
    if end - start < 1: # fewer than 2 elements
        return float('-inf')
    
    if end - start == 1: # only 2 elements
        return arr[start] + arr[end]**2
    
    mid = (start + end) // 2
    
    left_max = find_max_combination(arr, start, mid - 1)
    right_max = find_max_combination(arr, mid, end)
    

    ans = float('-inf')
    max_left = float('-inf')
    
    
    for i in range(start, mid): # Find maximum value in left half
        max_left = max(max_left, arr[i])
    
    
    for j in range(mid, end + 1): # Calculate max value using maximum from left half with each element in right half
        ans = max(ans, max_left + arr[j]**2)
    

    return max(left_max, right_max, ans)


def solve(arr):
    n = len(arr)
    return find_max_combination(arr, 0, n - 1)


n = int(input())
A = list(map(int, input().split()))


result = solve(A)
print(result)