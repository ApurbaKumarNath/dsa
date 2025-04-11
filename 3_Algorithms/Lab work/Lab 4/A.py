n, m = map(int, input().split())
adj_mat = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    u,v,w = map(int, input().split())
    adj_mat[u-1][v-1] = w # directed graph (converted 1-indexed to 0-indexed)

for row in adj_mat:
    print(" ".join(map(str, row)))
