import sys
sys.setrecursionlimit(2*10**5 + 10)

def dfs(u, adj, color, traversal_order):
    color[u] = 1 # Marked visited/Gray
    traversal_order.append(u) # Append the first element to the traversal order

    for v in adj[u]: # For each neighbor of u
        if color[v] == 0:
            dfs(v, adj, color, traversal_order)

n, m = map(int, input().split())
u_nodes = list(map(int, input().split()))
v_nodes = list(map(int, input().split()))

adj = [[] for _ in range(n + 1)] # 1-indexed adjacency list as 1st vertex is 1

for i in range(m): # Read m edges (u, v each) and build the adj. list
    u = u_nodes[i]
    v = v_nodes[i]
    adj[u].append(v)
    adj[v].append(u)

start_node = 1
traversal_order = []

color = [0] * (n + 1) # All vertices are initially white; 0: unvisited/white, 1: visited/Gray; 1-indexed
if color[start_node] == 0:
    dfs(start_node, adj, color, traversal_order)
print(" ".join(map(str, traversal_order))) # Print the traversal order

