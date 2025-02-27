N, K = input().split()
N, K = int(N), int(K)

numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

for j in range(K-1, -1, -1):
    print(numbers[j], end = ' ')