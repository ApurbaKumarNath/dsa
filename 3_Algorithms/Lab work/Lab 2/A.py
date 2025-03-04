def two_sum(arr, n, s):
    left = 0
    right = n - 1
    while left < right:
        if arr[left] + arr[right] == s:
            print(left + 1, right + 1)
            return

        elif arr[left] + arr[right] < s:
            left += 1
        else:
            right -= 1
    print(-1)

n, s = map(int, input().split())
arr = list(map(int, input().split()))

two_sum(arr, n, s)

