'''
There is an undirected unweighted graph with N nodes and M edges. The nodes are numbered from 1 to N. The i’th edge of this graph is between 
the i’th node in the second line and the i’th node in the third line, there is no self loop or multi edge. Find how many nodes and how many edges 
are reachable from the node numbered N, in O(N+M) time.

10 11:
12 12
1 1 1 2 2 2 3 3 7 4 12 11
2 3 4 5 6 7 8 9 1 12 5 10
'''

from collections import deque # Can use deque or list for stack in iterative DFS

# Setting a reasonable recursion depth is still good practice for DFS
import sys
try:
    # Set recursion depth higher for potentially deep paths
    # N+M might be around 1,000,000, so set it higher
    sys.setrecursionlimit(1000010)
except OverflowError:
    pass


# Using iterative DFS to avoid deep recursion issues entirely
def solve():
    N, M = map(int, input().split())

    # Read edges - handle potential empty input for M=0
    u_nodes = list(map(int, input().split())) if M > 0 else []
    v_nodes = list(map(int, input().split())) if M > 0 else []

    adj = [[] for _ in range(N + 1)]
    for i in range(M):
        u, v = u_nodes[i], v_nodes[i]
        adj[u].append(v) # Directed graph

    start_node = 1 # Assuming start node is 1 based on sample output

    # 0: White, 1: Gray, 2: Black
    color = [0] * (N + 1)
    reachable_nodes_count = 0
    reachable_edges_count = 0
    visited_edges = set() # Store visited edges as (u, v) tuples

    # Stack for iterative DFS
    stack = []

    # Initial push if start_node is valid
    if 1 <= start_node <= N:
         # We only start if the node hasn't been visited
         if color[start_node] == 0:
            stack.append(start_node)
            color[start_node] = 1 # Mark Gray immediately
            reachable_nodes_count += 1

    while stack:
        u = stack[-1] # Peek at the top node

        processed_neighbor = False # Flag to check if we found a new neighbor to push

        # Explore neighbors
        for v in adj[u]:
            edge = (u, v)
            # Add edge count only if this specific edge hasn't been counted
            if edge not in visited_edges:
                 reachable_edges_count += 1
                 visited_edges.add(edge)

            # If neighbor is unvisited (White)
            if color[v] == 0:
                color[v] = 1 # Mark Gray
                reachable_nodes_count += 1
                stack.append(v) # Push neighbor onto stack
                processed_neighbor = True
                break # Go deeper with the new node v

        # If we processed all neighbors of u or there were none
        if not processed_neighbor:
            stack.pop() # Pop u from stack
            color[u] = 2 # Mark Black - finished with this node

    return reachable_nodes_count, reachable_edges_count

# --- Main execution ---
#if __name__ == "__main__": # Standard practice in Python scripts
nodes_count, edges_count = solve()
print(nodes_count, edges_count)