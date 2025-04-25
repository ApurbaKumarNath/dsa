'''
Graph Metamorphosis
You are given a directed unweighted graph with N nodes in an adjacency list format. The nodes are numbered from 0 to N-1. 
Your task is to convert it into an adjacency matrix representation.

Input
The first line contains a integer N (1≤N≤100) — the number of vertices.

The next N lines describe the adjacency list:

The i-th line starts with an integer k, indicating the number of nodes adjacent to node i.
The next k space-separated integers represent the nodes adjacent to node i.
Nodes are numbered from 0 to N-1.
Output
Print an N×N adjacency matrix, where the cell at row i and column j
a. 1 if there is an edge between nodes i and j
b. 0 otherwise.
'''

n = int(input())
adj_mat = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    line = list(map(int, input().split()))
    k = line[0]
    for v in range(1, k+1): # v = vertex
        adj_mat[i][line[v]] = 1

for row in adj_mat:
    print(" ".join(map(str, row)))


