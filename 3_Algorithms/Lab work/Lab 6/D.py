'''
There is a tree with N nodes. The tree is rooted at a given node R.

You will be given Q queries. In each query, you are asked to find the size of the subtree of a given node X.

4 1
3 1
1 2
4 2
3
1
4
2

4
1
2
'''

# Increase recursion depth limit for deep trees (important for DFS)
import sys
sys.setrecursionlimit(200005) # N can be up to 2*10^5

# Global storage
adj = [] # Will be list of lists
subtree_size = []

# Depth First Search function_________________________________________________
def dfs(u, parent):
    # ... (DFS function remains exactly the same) ...
    global subtree_size
    current_subtree_size = 1
    for v in adj[u]:
        if v != parent:
            current_subtree_size += dfs(v, u)
    subtree_size[u] = current_subtree_size
    return current_subtree_size


# Main solve function_________________________________________________________
def solve():
    global adj, subtree_size
    N, R = map(int, input().split()) # N=nodes, R=root

    # Initialize adjacency list as a list of lists <<-- CHANGE HERE
    adj = [[] for _ in range(N + 1)]
    subtree_size = [0] * (N + 1) # Initialize size array (1-based index)

    # Build Adjacency List (Undirected Tree)________________________________
    for _ in range(N - 1): # A tree with N nodes has N-1 edges
        u, v = map(int, input().split())
        # Appending works the same way
        adj[u].append(v)
        adj[v].append(u)

    # Perform DFS starting from the root to compute all subtree sizes________
    # ... (Rest of the function remains exactly the same) ...
    dfs(R, 0)

    # Process Queries________________________________________________________
    Q = int(input())
    results = []
    for _ in range(Q):
        X = int(input())
        results.append(str(subtree_size[X])) # Look up precomputed size

    return "\n".join(results) # Return results separated by newline

# Main execution______________________________________________________________
output = solve()
print(output)