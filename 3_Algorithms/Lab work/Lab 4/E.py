'''
Edge Queries

You are given a directed unweighted graph with N nodes and M edges. The nodes are numbered from 1 to N. Your task is to find the difference of indegree and outdegree of each node in the graph.

Input
The first line contains two integers N and M (1≤N≤2×105,1≤M≤3×105) — the number of vertices and the total number of edges.

The second line contains M integers u1,u2,u3…um (1≤ui≤N) — where the i-th integer represents the node that is one endpoint of the i-th edge.

The third line contains M integers v1,v2,v3…vm (1≤vi≤N) — where the i-th integer represents the node that is other endpoint of the i-th edge.

The i-th edge of this graph is from the i-th node in the second line to the i-th node in the third line.

Output
Output a single line with N space-separated integers, where the i-th integer is the difference of indegree and outdegree of node i.
'''

n, m = map(int, input().split())
u_nodes, v_nodes = list(map(int, input().split())), list(map(int, input().split()))

in_degrees = [0] * (n + 1) # 1-based indexing
out_degrees = [0] * (n + 1)

for i in range(m):
    out_degrees[u_nodes[i]] += 1
    in_degrees[v_nodes[i]] += 1 # directed graph

for i in range(1, n + 1):
    print(in_degrees[i] - out_degrees[i], end = ' ') # difference of in and out degrees of every node