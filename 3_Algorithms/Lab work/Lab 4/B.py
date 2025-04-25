'''
Adjacency List Representation
You are given a directed weighted graph with N nodes and M edges. The nodes are numbered from 1 to N. Each edge represents a 
direct connection between two nodes. There is no self loop or multi edge.
'''

n, m = map(int, input().split())
if m > 0:
    u_nodes, v_nodes, w_nodes = list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split()))
else:
    u_nodes, v_nodes, w_nodes = [], [], []

adj_list = [[] for _ in range(n + 1)] # 1-indexed

for i in range(m):
    u = u_nodes[i]; v = v_nodes[i]; w = w_nodes[i]
    adj_list[u].append((v, w))  # directed graph (1-indexed)

for u in range(1, n + 1):
    print(f"{u}: ", end="")
    for v, w in adj_list[u]:
        print(f"({v}, {w})", end=" ")
    print()
    