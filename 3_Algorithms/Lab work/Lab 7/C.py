'''
You are in a city with N cities connected by M bi-directional roads. Each road has a danger level, where a higher number means the road is more dangerous.

You start in city 1 and need to go to every other city. The goal is to find the minimum danger level you would face to reach each city from city 1. 
The danger of a path is defined as the highest danger level of any road on that path.

For each city, find the minimum danger level of the path from city 1. If a city is not reachable from city 1, print −1. 
The danger of reaching city 1 is always 0.

4 3
2 1 3
2 3 5
3 4 3

0 3 5 5
'''

import heapq
import math

def solve():
    # Input Reading______________________________________________________________________________
    n, m = map(int, input().split())
    start_node = 0 # Problem states start is city 1 (index 0)

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1 # 0-based index
        v -= 1 # 0-based index
        # Bi-directional roads
        adj[u].append((v, w))
        adj[v].append((u, w))

    # Modified Dijkstra Initialization___________________________________________________________
    danger = [math.inf] * n    # Stores min-max danger to reach node i
    pq = []                    # Priority queue (min-heap)

    danger[start_node] = 0
    heapq.heappush(pq, (0, start_node)) # Store (max_danger_so_far, node)

    # Modified Dijkstra Main Loop________________________________________________________________
    while pq:
        current_max_danger, u = heapq.heappop(pq)

        # Optimization: If we found a path with lower max danger already, skip
        if current_max_danger > danger[u]:
            continue

        # Explore neighbors (Relaxation)
        for v, weight in adj[u]:
            # Calculate the max danger if we go through u to v
            new_max_danger_to_v = max(danger[u], weight)

            # If this path has a smaller bottleneck, update
            if new_max_danger_to_v < danger[v]:
                danger[v] = new_max_danger_to_v
                heapq.heappush(pq, (danger[v], v))

    # Output Generation_________________________________________________________________________
    result = []
    for i in range(n):
        if danger[i] == math.inf:
            result.append("-1")
        else:
            result.append(str(danger[i]))

    return " ".join(result)

# --- Main execution ---
result = solve()
print(result)