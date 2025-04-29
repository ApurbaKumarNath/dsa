'''
You are given an directed graph with N nodes and M edges. The graph contains no self-loops or multiple edges. The edges have no weight. 
The nodes are numbered from 1 to N and have a weight. You need to find the cost of a path, if there is any, from node S to node D with the minimum cost. 
The cost of a path is the sum of the weights of the nodes in that path.

4 3 1 2
3 4 5 4
1 2
3 2
4 3

7
'''

import heapq
import math

def solve():
    # Input Reading______________________________________________________________________________
    n, m, s_node, d_node = map(int, input().split())
    s_node -= 1 # 0-based index
    d_node -= 1 # 0-based index

    node_weights = list(map(int, input().split()))

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u - 1].append(v - 1) # Store only neighbor index, edges are unweighted

    # Modified Dijkstra Initialization___________________________________________________________
    d = [math.inf] * n         # Stores min cost (sum of node weights) to reach node i
    pq = []                    # Priority queue (min-heap)

    # Cost to reach start node is its own weight
    if s_node < n: # Basic check
         d[s_node] = node_weights[s_node]
         heapq.heappush(pq, (d[s_node], s_node)) # Store (current_path_cost, node)
    else:
         # Handle cases where S might be out of bounds based on constraints
         # Though problem constraints likely prevent this
         pass


    # Modified Dijkstra Main Loop________________________________________________________________
    while pq:
        current_cost, u = heapq.heappop(pq)

        # Optimization: If we found a lower cost path already, skip
        if current_cost > d[u]:
            continue

        # If we reached the destination, we can potentially stop early (optional)
        # if u == d_node:
        #     break

        # Explore neighbors (Relaxation)
        for v in adj[u]:
            # Calculate the cost if we go through u to v
            # Cost = (cost up to u) + (weight of node v)
            potential_cost = d[u] + node_weights[v]

            # If this path has a lower total node weight sum, update
            if potential_cost < d[v]:
                d[v] = potential_cost
                heapq.heappush(pq, (d[v], v))

    # Output Generation_________________________________________________________________________
    final_cost = d[d_node]

    if final_cost == math.inf:
        return "-1"
    else:
        return str(final_cost)

# --- Main execution ---
result = solve()
print(result)