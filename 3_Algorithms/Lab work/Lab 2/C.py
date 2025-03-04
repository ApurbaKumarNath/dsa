def longest_subarray_sum(n, k, arr):
    left = 0
    best_left = 0
    best_right = 0
    sum = 0 # current sum
    length = 0

    for right in range(n):
        sum += arr[right]
        
        while sum > k and left <= right:
            sum -= arr[left]
            left += 1

        if sum <= k and length < (right - left + 1):
            best_left = left
            best_right = right
            length = right - left + 1

    return length


n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(longest_subarray_sum(n, k, arr))