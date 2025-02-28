N, K = map(int, input().split())

numbers = input().split()

print(' '.join(numbers[K-1: -len(numbers) - 1: -1]))