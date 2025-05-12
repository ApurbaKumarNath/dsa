def solve():
    n, k = map(int, input().split())

    # DSU Initialization_______________________________________________________________________
    # parent[i] stores the parent of element i (1-indexed)
    # size[i] stores the size of the set if i is the representative
    parent = list(range(n + 1)) # parent[i] = i initially
    set_size = [1] * (n + 1)    # size[i] = 1 initially
    set_size[0] = 0             # 0th index not used

    results = []

    # DSU Find Operation (with Path Compression)_______________________________________________
    def find_set(v):
        if v == parent[v]:
            return v
        parent[v] = find_set(parent[v]) # Path compression
        return parent[v]

    # DSU Union Operation (by Size)____________________________________________________________
    def union_sets(a, b):

        a_root = find_set(a)
        b_root = find_set(b)
        if a_root != b_root: # Union by size: attach smaller tree under root of larger tree
             
            if set_size[a_root] > set_size[b_root]:
                 
                parent[b_root] = a_root
                set_size[a_root] += set_size[b_root]

            else:
                parent[a_root] = b_root
                set_size[b_root] += set_size[a_root]

        return set_size[find_set(a_root)] # Return the size of the set after union

    # Processing Friendships__________________________________________________________________
    for _ in range(k):
        p1, p2 = map(int, input().split())
        results.append(str(union_sets(p1, p2)))

    return "\n".join(results)

# --- Main execution ---
output_str = solve()
print(output_str)