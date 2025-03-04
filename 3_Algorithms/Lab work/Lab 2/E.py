def count_in_queries(n, arr, queries):
    for q in queries:
        # find leftmost element >= q[0] using binary search
        left = 0
        right = n - 1
        left_idx = 0

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] >= q[0]:
                left_idx = mid
                right = mid - 1

            else:
                left = mid + 1

        # find rightmost element > q[1] using binary search
        left = 0
        right = n - 1
        right_idx = n

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] <= q[1]:
                left = mid + 1

            else:
                right_idx = mid
                right = mid - 1

        print(right_idx - left_idx)




n, q = map(int, input().split())
arr = list(map(int, input().split()))
queries = []
for i in range(q):
    queries.append(list(map(int, input().split())))
count_in_queries(n, arr, queries)