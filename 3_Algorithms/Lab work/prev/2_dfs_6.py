'''
There is a directed unweighted graph with N nodes and M edges. The nodes are numbered from 1 to N. The i’th edge of this graph is from the i’th 
node in the second line to the i’th node in the third line, there is no self loop or multi edge. A simple cycle is a path which starts and ends 
at the same node such that no edge is present more than once in that path. Find if there is any simple cycle in this graph, and if there is then 
find any such cycle. Do everything in O(N+M) time.

1 2 7 1:
12 12
1 1 1 2 2 2 3 3 7 4 12 11
2 3 4 5 6 7 8 9 1 12 5 10
'''

from collections import deque # Although not strictly needed for recursive DFS, it's good practice

# Increase recursion depth limit for potentially deep DFS paths
# Using try-except for compatibility if setting limit fails
try:
    import sys
    sys.setrecursionlimit(500010 * 2) # Set higher than N+M
except (ImportError, OverflowError):
    pass # Ignore if sys module or setting limit isn't available/allowed

def dfs_find_cycle(u, adj, color, parent):
    """
    Performs DFS to detect cycles. Uses recursion.
    Returns the cycle path list if found, otherwise None.
    color: 0=White, 1=Gray, 2=Black
    """
    color[u] = 1 # Mark current node as visiting (Gray)

    for v in adj[u]: # Explore neighbors
        if color[v] == 1: # Neighbor is Gray - Cycle detected!
            # Reconstruct the cycle path
            cycle_path = [v] # Start with the node where cycle rejoins
            curr = u
            while curr != v: # Go backwards from u until we hit v again
                cycle_path.append(curr)
                curr = parent[curr]
                if curr == -1: # Should not happen in a detected cycle
                    # Fallback or error if needed, but indicates logic issue
                    return None # Or raise error
            cycle_path.append(v) # Add the start node again to close cycle
            cycle_path.reverse() # Put in traversal order (v -> ... -> u -> v)
            return cycle_path # Return the found cycle

        elif color[v] == 0: # Neighbor is White - Recurse
            parent[v] = u # Remember we came from u
            found_cycle = dfs_find_cycle(v, adj, color, parent)
            if found_cycle: # If the recursive call found a cycle
                return found_cycle # Propagate the finding upwards

        # If color[v] == 2 (Black), do nothing, already explored.

    color[u] = 2 # Mark as fully processed (Black)
    return None # No cycle found starting from this path segment

def solve():
    # --- 1. Read Input ---
    n, m = map(int, input().split())

    # Handle case with no edges immediately
    if m == 0:
        return "0"

    u_nodes = list(map(int, input().split()))
    v_nodes = list(map(int, input().split()))

    # --- 2. Build Adjacency List (Directed) ---
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v = u_nodes[i], v_nodes[i]
        # Avoid adding self-loops if strictly following problem rules (though not in examples)
        if u != v:
             adj[u].append(v) # Directed edge u -> v

    # --- 3. Initialize Colors and Parent array ---
    color = [0] * (n + 1) # 0: White, 1: Gray, 2: Black
    parent = [-1] * (n + 1) # Store parent pointers for path reconstruction
    final_cycle_path = None

    # --- 4. Iterate Through All Nodes ---
    # Necessary if the graph is not fully connected
    for i in range(1, n + 1):
        if color[i] == 0: # If node hasn't been visited yet
            # Start DFS from this node
            result_path = dfs_find_cycle(i, adj, color, parent)
            if result_path: # If DFS found a cycle
                final_cycle_path = result_path
                break # Found one cycle, no need to search further

    # --- 5. Format Output ---
    if final_cycle_path:
        # Convert nodes to strings and join with spaces
        return " ".join(map(str, final_cycle_path))
    else:
        return "0"

# --- Run the solver ---
result = solve()
print(result) # The main part of the script prints the returned value