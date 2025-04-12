import math
n, q = map(int, input().split())
adj_list = [[] for _ in range(n + 1)] # 1-indexed adjacency list

# if gcd == 1, they're coprime & neighbors
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if math.gcd(i, j) == 1:
            adj_list[i].append(j)
            adj_list[j].append(i)

for _ in range(q):
    x, k = map(int, input().split())
    if 1 <= k <= len(adj_list[x]):
        print(adj_list[x][k - 1]) # k-1 because of 0-indexing
    else:
        print(-1)
    