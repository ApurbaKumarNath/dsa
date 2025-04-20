import sys
sys.setrecursionlimit(2*10**5 + 10)

def dfs_cycle(u, adj, color):
    color[u] = 1

    for v in adj[u]:
        if color[v] == 1: # Gray to Gray (Back edge); cycle detected
            return True
        if color[v] == 0:
            if dfs_cycle(v, adj, color): # Recursive call to check for cycles
                return True
    
    color[u] = 2 # Mark as Black (visited); no adj. vertices left to explore
    return False # No cycle detected

N, M = map(int, input().split())

adj = [[] for _ in range(N + 1)] # 1-indexed adjacency list
for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v) # directed graph

color = [0] * (N + 1) # 0: unvisited/white, 1: visited/Gray, 2: visited/Black
has_cycle = False

for u in range(1, N + 1):
    if color[u] == 0: # If the vertex is unvisited
        if dfs_cycle(u, adj, color): # Check for cycles
            has_cycle = True
            print("YES")
            break

if not has_cycle:
    print("NO") # No cycles detected
