n = int(input())
adj_mat = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    line = list(map(int, input().split()))
    k = line[0]
    for v in range(1, k+1): # v = vertex
        adj_mat[i][line[v]] = 1

for row in adj_mat:
    print(" ".join(map(str, row)))


