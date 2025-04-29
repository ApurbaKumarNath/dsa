'''
You are given an directed weighted graph with N nodes and M edges. The nodes are numbered from 1 to N. The graph contains no self-loops or multiple edges.

There is a source and a destination. Your task is to find the shortest distance from the source node to the destination node and print the path taken. 
If multiple shortest paths exist, print any one of them. If no such path exists, print −1.

4 3 4 2
1 3 4
2 2 3
3 4 5

9
4 3 2
'''

import heapq
import math # Using math.inf instead of float('inf') for consistency

def solve():
    # Input Reading______________________________________________________________________________
    line1 = input().split()
    n, m, s_node, d_node = map(int, line1)
    s_node -= 1 # Adjust to 0-based index
    d_node -= 1 # Adjust to 0-based index

    adj = [[] for _ in range(n)] # Adjacency list: adj[u] = [(v, weight), ...]

    # Read edge endpoints u and v
    u_nodes = list(map(int, input().split()))
    v_nodes = list(map(int, input().split()))
    weights = list(map(int, input().split()))

    # Populate adjacency list (adjusting to 0-based index)
    for i in range(m):
        u = u_nodes[i] - 1
        v = v_nodes[i] - 1
        w = weights[i]
        # The problem statement says: "The i-th edge of this graph is from
        # the i-th node in the second line to the i-th node in the third line"
        # This implies a directed edge u -> v
        adj[u].append((v, w))

    # Dijkstra Initialization____________________________________________________________________
    d = [math.inf] * n      # Distance array
    parent = [-1] * n       # Parent array for path reconstruction
    pq = []                 # Priority queue (min-heap)

    d[s_node] = 0
    heapq.heappush(pq, (0, s_node)) # Store (distance, node)

    # Dijkstra Main Loop________________________________________________________________________
    while pq:
        dist_u, u = heapq.heappop(pq)

        if dist_u > d[u]:
            continue

        # Optimization: If we reached the destination, we can potentially stop
        if u == d_node: # This optimization works only if edge weights are non-negative
            break       # However, let it run fully to ensure correctness for all cases

        # Explore neighbors (Relaxation)
        for v, weight in adj[u]:
            if d[u] + weight < d[v]:
                d[v] = d[u] + weight
                parent[v] = u
                heapq.heappush(pq, (d[v], v))

    # Output Generation_________________________________________________________________________
    if d[d_node] == math.inf:
        return "-1"
    else:
        # Path Reconstruction
        path = []
        curr = d_node
        while curr != -1:
            path.append(curr + 1) # Store 1-based index for output
            curr = parent[curr]
        path.reverse() # Reverse to get path from S to D

        # Format output
        result_dist = str(d[d_node])
        result_path = " ".join(map(str, path))
        return f"{result_dist}\n{result_path}"

# --- Main execution ---
result = solve()
print(result)