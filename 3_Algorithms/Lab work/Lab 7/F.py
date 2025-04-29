'''
You are given a bidirectional weighted graph with N nodes and M edges. The nodes are numbered from 1 to N. The graph contains no self-loops or multiple edges.
There is a source and a destination. Your task is to find the cost of the second shortest path from the source node to the destination node. 
If no such path exists, print −1.

Note: Second shortest path will be strictly greater than the shortest path

4 3 2 3
2 1 3
2 3 5
3 4 3

11
'''

import heapq
import math

def run_dijkstra(start_node, n, adj):
    """
    Runs Dijkstra from a given start_node.
    Returns a list of shortest distances from start_node to all other nodes.
    """
    d = [math.inf] * n
    pq = []

    d[start_node] = 0
    heapq.heappush(pq, (0, start_node)) # (distance, node)

    while pq:
        dist_u, u = heapq.heappop(pq)

        if dist_u > d[u]:
            continue

        for v, weight in adj[u]:
            if d[u] + weight < d[v]:
                d[v] = d[u] + weight
                heapq.heappush(pq, (d[v], v))
    return d

def solve():
    # Input Reading______________________________________________________________________________
    n, m, s_node, d_node = map(int, input().split())
    s_node -= 1 # 0-based index
    d_node -= 1 # 0-based index

    adj = [[] for _ in range(n)]
    edges = [] # Store edges explicitly to iterate later
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        # Bidirectional edges
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w)) # Store the connection details

    # Run Dijkstra from Source and Destination_________________________________________________
    d_from_s = run_dijkstra(s_node, n, adj)
    d_from_d = run_dijkstra(d_node, n, adj)

    # Get Shortest Path Cost___________________________________________________________________
    shortest_cost = d_from_s[d_node]

    # Check Reachability
    if shortest_cost == math.inf:
        return "-1"

    # Find Second Shortest Path Candidate______________________________________________________
    second_shortest_cost = math.inf

    # Iterate through all original connections (edges)
    for u, v, w in edges:
        # Consider path S -> u -> v -> D
        if d_from_s[u] != math.inf and d_from_d[v] != math.inf:
            candidate_cost1 = d_from_s[u] + w + d_from_d[v]
            if candidate_cost1 > shortest_cost:
                second_shortest_cost = min(second_shortest_cost, candidate_cost1)

        # Consider path S -> v -> u -> D (redundant if adj list built symmetrically, but safe)
        if d_from_s[v] != math.inf and d_from_d[u] != math.inf:
             candidate_cost2 = d_from_s[v] + w + d_from_d[u]
             if candidate_cost2 > shortest_cost:
                 second_shortest_cost = min(second_shortest_cost, candidate_cost2)


    # Output Generation_________________________________________________________________________
    if second_shortest_cost == math.inf:
        return "-1" # No path strictly greater than the shortest was found
    else:
        return str(second_shortest_cost)

# --- Main execution ---
result = solve()
print(result)