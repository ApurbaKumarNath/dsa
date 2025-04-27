'''
You are given an undirected connected graph with N nodes and N−1 edges. 
Your task is to find two nodes such that the path between those two nodes is the longest possible in the graph.

5
5 1
1 4
4 2
3 2

4
3 5
'''

import sys
sys.setrecursionlimit(200005) # N can be up to 200000

# Global variables to store DFS results
adj = []
max_dist = -1       # Stores the maximum distance found in a DFS run
farthest_node = -1  # Stores the node at the maximum distance

# Depth First Search function_________________________________________________
def dfs(u, parent, current_dist):
    """
    Performs DFS to find the farthest node from the starting node 'u'.
    Updates global max_dist and farthest_node.
    Args:
        u: Current node being visited.
        parent: The node from which we reached u (to avoid going back).
        current_dist: The distance from the initial start of this DFS run to u.
    """
    global max_dist, farthest_node

    # Check if this node is farther than the current maximum
    if current_dist > max_dist:
        max_dist = current_dist
        farthest_node = u

    # Visit neighbors
    for v in adj[u]:
        if v != parent: # Don't go back up
            dfs(v, u, current_dist + 1) # Recurse with incremented distance

# Main solve function_________________________________________________________
def solve():
    global adj, max_dist, farthest_node
    N = int(input())

    # Initialization_________________________________________________________
    adj = [[] for _ in range(N + 1)] # Use 1-based indexing

    # Build Adjacency List (Undirected Tree)________________________________
    for _ in range(N - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    # First DFS run (from arbitrary node 1)_________________________________
    max_dist = -1
    farthest_node = -1
    dfs(1, 0, 0) # Start DFS from node 1, parent 0, distance 0
    endpoint1 = farthest_node # Store the endpoint found

    # Second DFS run (from the farthest node found above)____________________
    max_dist = -1
    farthest_node = -1
    dfs(endpoint1, 0, 0) # Start DFS from endpoint1
    endpoint2 = farthest_node # Store the other endpoint
    diameter_length = max_dist # The max distance from the second run

    # Format and return result______________________________________________
    # Ensure endpoints are returned in a consistent order (optional, but good practice)
    if endpoint1 > endpoint2:
        endpoint1, endpoint2 = endpoint2, endpoint1

    return f"{diameter_length}\n{endpoint1} {endpoint2}"

# Main execution______________________________________________________________
output = solve()
print(output)