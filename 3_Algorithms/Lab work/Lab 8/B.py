# We need a list to store edges: (cost, u, v)
# DSU structures: parent, set_size
# DSU functions: find_set, union_sets (using union by size)

def solve():
    n, m = map(int, input().split())

    # DSU Initialization_______________________________________________________________________
    parent = list(range(n + 1)) # 1-indexed
    set_size = [1] * (n + 1)
    set_size[0] = 0 # Not used

    # DSU Find Operation (with Path Compression)_______________________________________________
    def find_set(v_node): # Renamed v to v_node to avoid conflict with edge's v
        if v_node == parent[v_node]:
            return v_node
        parent[v_node] = find_set(parent[v_node])
        return parent[v_node]

    # DSU Union Operation (by Size)____________________________________________________________
    def union_sets(a_node, b_node): # Renamed a,b to avoid conflict
        a_root = find_set(a_node)
        b_root = find_set(b_node)
        if a_root != b_root:
            if set_size[a_root] < set_size[b_root]: # Attach smaller to larger
                a_root, b_root = b_root, a_root
            parent[b_root] = a_root
            set_size[a_root] += set_size[b_root]
            return True # Union performed
        return False # Already in the same set

    # Read and Store Edges____________________________________________________________________
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u, v)) # Store as (cost, u, v) for easy sorting by cost

    # Sort Edges by Cost_______________________________________________________________________
    edges.sort()

    # Kruskal's Algorithm Main Loop____________________________________________________________
    mst_cost = 0
    edges_count_in_mst = 0

    for cost, u, v in edges:
        if edges_count_in_mst == n - 1: # MST is complete
            break

        if union_sets(u, v): # If u and v were in different sets (union happened)
            mst_cost += cost
            edges_count_in_mst += 1

    # Output Generation_________________________________________________________________________
    # The problem implies the graph is always connected, so an MST will always be found
    # with n-1 edges if M >= N-1.
    return str(mst_cost)

# --- Main execution ---
result = solve()
print(result)