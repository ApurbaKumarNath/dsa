'''
You are given a directed weighted graph with N nodes and M edges. The nodes are numbered from 1 to N. The graph contains no self-loops or multiple edges.
Your task is to find the shortest distance from node 1 to node N, with an additional constraint: the path cannot contain two consecutive 
edges with the same parity (i.e., both even or both odd). If no such path exists, print −1.

4 3
1 3 2
4 4 3
3 4 5

3
'''

import heapq
import math

def solve():
    # Input Reading______________________________________________________________________________
    # Assuming Problem A's input format based on the example structure
    line1 = input().split()
    if len(line1) == 2: # Format N M
        n, m = map(int, line1)
        start_node = 0
        dest_node = n - 1
    else: # Fallback if format is different, adapt as needed
        # Handle other potential formats if necessary
        print("Unknown input format")
        return "-1" # Or raise error


    adj = [[] for _ in range(n)]

    # Determine input format for edges
    # Let's assume standard M lines of u v w first

    u_nodes = list(map(int, input().split()))
    v_nodes = list(map(int, input().split()))
    weights = list(map(int, input().split()))

    for i in range(m):
        u = u_nodes[i] - 1
        v = v_nodes[i] - 1
        w = weights[i]
        adj[u].append((v, w)) # Directed edge



    # Modified Dijkstra Initialization___________________________________________________________
    # d[node][parity]: min cost to reach node ending with edge of parity (0=even, 1=odd)
    d = [[math.inf] * 2 for _ in range(n)]
    pq = []  # Stores (cost, current_node, parity_of_last_edge)

    # Process edges starting from source node 0
    for v, w in adj[start_node]:
        parity = w % 2
        if w < d[v][parity]:
            d[v][parity] = w
            heapq.heappush(pq, (w, v, parity))

    # Modified Dijkstra Main Loop________________________________________________________________
    while pq:
        cost_u, u, parity_in = heapq.heappop(pq)

        # If this path is worse than one already found, skip
        if cost_u > d[u][parity_in]:
            continue

        # Explore neighbors
        for v, w in adj[u]:
            parity_out = w % 2

            # Check Parity Constraint: next edge must have different parity
            if parity_out != parity_in:
                new_cost = d[u][parity_in] + w

                # Relaxation: If this path is better for the target state (v, parity_out)
                if new_cost < d[v][parity_out]:
                    d[v][parity_out] = new_cost
                    heapq.heappush(pq, (new_cost, v, parity_out))

    # Output Generation_________________________________________________________________________
    final_cost = min(d[dest_node][0], d[dest_node][1])

    if final_cost == math.inf:
        return "-1"
    else:
        return str(final_cost)

# --- Main execution ---
result = solve()
print(result)