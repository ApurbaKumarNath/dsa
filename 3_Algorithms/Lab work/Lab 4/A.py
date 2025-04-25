'''
Adjacency Matrix Representation
You are given a directed weighted graph with N nodes and M edges. The nodes are numbered from 1 to N. Each edge represents a direct 
connection between two nodes. There is no self loop or multi edge.
'''

n, m = map(int, input().split())
adj_mat = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    u,v,w = map(int, input().split())
    adj_mat[u-1][v-1] = w # directed graph (converted 1-indexed to 0-indexed)

for row in adj_mat:
    print(" ".join(map(str, row)))
