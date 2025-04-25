'''
Coprime Graph
You are given an integer N. Construct an undirected graph with N nodes, where each node i is connected to all node j such that gcd(i,j)=1 
where 1≤i,j≤N and i!=j.
For example,for N=6, the graph will be, G=[[2,3,4,5,6],[1,3,5],[1,2,4,5],[1,3,5],[1,2,3,4,6],[1,5]].
Now, there will be Q queries. Each query consists of two integers X and K. For each query, you have to determine the K−th smallest node connected to node X.
'''

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
    