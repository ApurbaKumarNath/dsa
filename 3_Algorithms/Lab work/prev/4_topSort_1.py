'''
There are N integers: 0, 1, … (N-1). Also, there are M rules: (X[0], Y[0]), (X[1], Y[1]), … (X[M-1], Y[M-1]). Find the lexicographically 
largest permutation of the N integers such that for each of the rules (X[i], Y[i]), X[i] comes before Y[i] in the permutation. If there is no 
such permutation then detect that.
'''

import heapq # heapq implements a min-heap, we'll use negative values for max-heap behavior

def solve():
    N, M = map(int, input().split())

    # Handle case where M=0 separately for cleaner logic below
    if M == 0:
        # No rules, largest permutation is N-1 down to 0
        return list(range(N - 1, -1, -1))

    # Read X and Y lists
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))

    # --- Build Graph and Calculate In-degrees ---
    adj = [[] for _ in range(N)] # Adjacency list for nodes 0 to N-1
    in_degree = [0] * N        # In-degree for nodes 0 to N-1

    for i in range(M):
        u, v = X[i], Y[i]
        # Add edge u -> v
        adj[u].append(v)
        # Increment in-degree of the destination node v
        in_degree[v] += 1

    # --- Initialize Max-Priority Queue ---
    # Use negative values because heapq is a min-heap
    priority_queue = []
    for i in range(N):
        if in_degree[i] == 0:
            heapq.heappush(priority_queue, -i) # Push negative of the node index

    # --- Process Nodes (Topological Sort) ---
    result = []
    while priority_queue:
        # Extract the largest node (smallest negative value)
        neg_u = heapq.heappop(priority_queue)
        u = -neg_u # Get the actual node index back
        result.append(u)

        # Process neighbors
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                heapq.heappush(priority_queue, -v) # Push negative of the neighbor

    # --- Check for Cycles and Return Result ---
    if len(result) == N:
        return result # Successfully sorted all nodes
    else:
        return -1     # Cycle detected, not all nodes could be processed

# --- Get the result from the solve function ---
output = solve()

# --- Print the output ---
if output == -1:
    print("-1")
else:
    # Print list elements separated by spaces
    print(*(output)) # The '*' unpacks the list for printing