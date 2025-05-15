import math
# It's good practice to set a higher recursion limit for DSU if N can be large,
# though for N=1000, the default might be okay with path compression.
# import sys
# sys.setrecursionlimit(2 * 10**5) # N=10^3 means path length can be at most N

# DSU Data Structures (Global or passed around, let's make them part of kruskal_mst scope)
# parent_arr
# size_arr

# DSU Find Operation (with Path Compression)_______________________________________________
def find_op(p_arr, i): # p_arr is parent_arr
    if p_arr[i] == i:
        return i
    p_arr[i] = find_op(p_arr, p_arr[i])
    return p_arr[i]

# DSU Union Operation (by Size)____________________________________________________________
def union_op(p_arr, s_arr, i, j): # s_arr is size_arr
    root_i = find_op(p_arr, i)
    root_j = find_op(p_arr, j)

    if root_i != root_j:
        # Union by size: attach smaller tree under root of larger tree
        if s_arr[root_i] < s_arr[root_j]:
            p_arr[root_i] = root_j
            s_arr[root_j] += s_arr[root_i]
        else:
            p_arr[root_j] = root_i
            s_arr[root_i] += s_arr[root_j]
        return True # Union occurred
    return False # Already in the same set

# Kruskal's Algorithm to find MST__________________________________________________________
def get_mst(n_nodes, all_edges_list):
    # Sort edges by weight: (weight, u, v)
    # Using a simple sort without lambda, assuming edges are stored as (w, u, v)
    # If edges are (u,v,w), then we'd need a custom sort or store differently.
    # Let's assume all_edges_list contains (w, u, v) tuples already.
    # If not, we'd convert: temp_edges = [(w,u,v) for u,v,w in all_edges_list]; temp_edges.sort()
    
    # For simplicity, assuming all_edges_list is already list of (w, u, v)
    # and if it's not, the calling code should format it.
    # In this problem, the input is u, v, w, so we'll make (w, u, v) and then sort.

    p_arr = list(range(n_nodes + 1)) # 1-indexed
    s_arr = [1] * (n_nodes + 1)
    s_arr[0] = 0

    current_mst_edges = []
    current_mst_weight = 0
    edges_in_tree = 0

    for w, u, v in all_edges_list: # Assumes all_edges_list is sorted by w
        if find_op(p_arr, u) != find_op(p_arr, v):
            union_op(p_arr, s_arr, u, v)
            current_mst_edges.append((u, v, w)) # Store original u,v,w for identification
            current_mst_weight += w
            edges_in_tree += 1
            if edges_in_tree == n_nodes - 1:
                break
    
    if edges_in_tree < n_nodes - 1: # Graph not connected
        return None, -1 # Or handle error as problem expects

    return current_mst_edges, current_mst_weight


def solve():
    # Input Reading______________________________________________________________________________
    n, m = map(int, input().split()) # n = nodes, m = edges

    original_edges = [] # List to store (u, v, w)
    edges_for_kruskal = [] # List to store (w, u, v) for sorting
    
    for _ in range(m):
        u, v, w = map(int, input().split())
        original_edges.append((u, v, w))
        edges_for_kruskal.append((w, u, v))
    
    edges_for_kruskal.sort() # Sort by weight

    # Step 1: Calculate the first MST_________________________________________________________
    mst1_edges, mst1_weight = get_mst(n, edges_for_kruskal)

    if mst1_edges is None: # Should not happen based on problem statement (graph is connected)
        return "-1"
    if len(mst1_edges) < n - 1: # If not enough edges for MST (disconnected)
        return "-1"


    min_second_mst_weight = math.inf

    # Step 2: Iterate through each edge in MST1________________________________________________
    for i in range(len(mst1_edges)):
        # Temporarily remove mst1_edges[i]
        edge_to_remove_u, edge_to_remove_v, edge_to_remove_w = mst1_edges[i]

        # Build a DSU state with MST1 minus the edge_to_remove
        # This DSU will represent the two components formed.
        p_temp = list(range(n + 1))
        s_temp = [1] * (n + 1)
        s_temp[0] = 0
        
        current_temp_tree_weight = 0
        edges_for_temp_tree = 0

        for k in range(len(mst1_edges)):
            if i == k: # Skip the edge we are "removing"
                continue
            
            u_mst, v_mst, w_mst = mst1_edges[k]
            # No need to check find_op here, these edges form a tree (or two trees)
            if find_op(p_temp, u_mst) != find_op(p_temp, v_mst): # ensure union if distinct
                union_op(p_temp, s_temp, u_mst, v_mst)
                current_temp_tree_weight += w_mst # This weight is not directly used for final sum
                edges_for_temp_tree +=1

        # Now, try to add a replacement edge from original_edges
        # The replacement edge must connect the two components.
        # The replacement edge must not be the same as edge_to_remove.
        
        for orig_u, orig_v, orig_w in original_edges:
            # Check if this edge is the one we removed (to avoid re-adding it)
            # Need to check both (u,v) and (v,u) if original edges are not canonical
            is_removed_edge = ( (orig_u == edge_to_remove_u and orig_v == edge_to_remove_v) or \
                                (orig_u == edge_to_remove_v and orig_v == edge_to_remove_u) ) \
                              and orig_w == edge_to_remove_w 
            if is_removed_edge:
                continue

            # Check if this edge connects the two components
            if find_op(p_temp, orig_u) != find_op(p_temp, orig_v):
                candidate_mst2_weight = mst1_weight - edge_to_remove_w + orig_w
                
                if candidate_mst2_weight > mst1_weight:
                    min_second_mst_weight = min(min_second_mst_weight, candidate_mst2_weight)

    # Output Generation_________________________________________________________________________
    if min_second_mst_weight == math.inf:
        return "-1"
    else:
        return str(min_second_mst_weight)

# --- Main execution ---
result = solve()
print(result)