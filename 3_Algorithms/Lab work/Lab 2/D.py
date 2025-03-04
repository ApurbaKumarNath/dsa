def find_leftmost_1(arr):
    for bin in arr:
        left = 0
        right = len(bin) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2

            if bin[mid] == '1':
                result = mid + 1
                right = mid - 1
            else:
                left = mid + 1
        print(result)


t = int(input())
binary_str = []
for i in range(t):
    binary_str.append(input())

find_leftmost_1(binary_str)