'''
There is an undirected unweighted graph with N nodes and M edges. The nodes are numbered from 1 to N. The i’th edge of this graph is 
between the i’th node in the second line and the i’th node in the third line, there is no self loop or multi edge. Find the minimum 
number of edges (and any valid set of such edges) that you need to remove from this graph such that after the modification there is 
no cycle in this graph. Do everything in O(N+M) time.

0:
6 4
6 2 3 5
2 3 4 1

2
1 1
2 7:
12 12
1 1 1 2 2 2 3 3 7 4 12 11
2 3 4 5 6 7 8 9 1 12 5 10
'''

from collections import deque # Not strictly needed for DSU, but good habit

# --- DSU Functions ---
# parent array will be global or passed around; let's pass it

def find_set(v, parent):
    """Finds the representative of the set containing v, with path compression."""
    if v == parent[v]:
        return v
    # Path compression: Make node point directly to the root
    parent[v] = find_set(parent[v], parent)
    return parent[v]

def unite_sets(a, b, parent):
    """Merges the sets containing a and b."""
    a_root = find_set(a, parent)
    b_root = find_set(b, parent)
    if a_root != b_root:
        # Make the root of a's set the parent of the root of b's set
        parent[b_root] = a_root
        return True # Indicate that a union happened
    return False # Indicate that they were already in the same set

# --- Main Solver ---
def solve():
    N, M = map(int, input().split())

    # Read endpoint lists - handle M=0 case
    u_nodes = list(map(int, input().split())) if M > 0 else []
    v_nodes = list(map(int, input().split())) if M > 0 else []

    # Initialize DSU parent array (1-based indexing)
    parent = list(range(N + 1))

    # Store the endpoints of edges that cause cycles
    removed_u = []
    removed_v = []

    # Process each edge
    for i in range(M):
        u = u_nodes[i]
        v = v_nodes[i]

        # Find the representatives of the sets containing u and v
        u_root = find_set(u, parent)
        v_root = find_set(v, parent)

        # If they are in the same set, adding this edge creates a cycle
        if u_root == v_root:
            removed_u.append(u)
            removed_v.append(v)
        else:
            # Otherwise, unite the sets (add edge to the spanning forest)
            unite_sets(u_root, v_root, parent) # Pass roots to unite_sets

    # --- Prepare Output ---
    result = []
    count = len(removed_u)
    result.append(str(count))

    if count > 0:
        result.append(" ".join(map(str, removed_u)))
        result.append(" ".join(map(str, removed_v)))

    return result

# --- Run and Print ---
output_lines = solve()
for line in output_lines:
    print(line)