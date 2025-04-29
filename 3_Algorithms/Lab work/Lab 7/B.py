'''
Alice and Bob are in a hurry to meet each other and have to traverse through a directed graph with weighted edges. The nodes are numbered from 1 to N. 
The graph contains no self-loops or multiple edges.

Alice starts from node S and Bob starts from node T. They want to find a common node in the graph where they can meet each other 
in the minimum amount of time. Alice or Bob can wait at any node if they want to.

5 5 1 5
1 2 1
2 3 1
5 3 2
1 4 2
5 4 2

2 3
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
    n, m, s_node, t_node = map(int, input().split())
    s_node -= 1 # 0-based index
    t_node -= 1 # 0-based index

    adj = [[] for _ in range(n)]
    # The PDF for Problem B specifies M lines each with u, v, w
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u - 1].append((v - 1, w)) # Directed edge u->v

    # Run Dijkstra for Alice and Bob___________________________________________________________
    d_alice = run_dijkstra(s_node, n, adj)
    d_bob = run_dijkstra(t_node, n, adj)

    # Find the best meeting node________________________________________________________________
    min_max_time = math.inf
    best_node_idx = -1

    for k in range(n):
        # Check if node k is reachable by both
        if d_alice[k] != math.inf and d_bob[k] != math.inf:
            current_max_time = max(d_alice[k], d_bob[k])

            # Update minimum maximum time and best node
            if current_max_time < min_max_time:
                min_max_time = current_max_time
                best_node_idx = k
            elif current_max_time == min_max_time:
                # If times are equal, choose the node with the smaller index
                if best_node_idx == -1 or k < best_node_idx:
                     best_node_idx = k

    # Output Generation_________________________________________________________________________
    if best_node_idx == -1:
        return "-1"
    else:
        # Return time and 1-based node index
        return f"{min_max_time} {best_node_idx + 1}"

# --- Main execution ---
result = solve()
print(result)