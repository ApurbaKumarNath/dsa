'''
There is an undirected unweighted graph with N nodes and M edges. The nodes are numbered from 1 to N. The i’th edge of this graph is 
between the i’th node in the second line and the i’th node in the third line, there is no self loop or multi edge. There are two colors: 
A and B. Find if it is possible to assign each node any of these two colors such that no two adjacent nodes have the same color, and if 
possible then find any such coloring. Do everything in O(N+M) time.
'''


from collections import deque

def solve():
    """
    Checks if a graph is bipartite and returns a 2-coloring or 'X'.
    Uses standard 'u v' input for edges.
    """
    N, M = map(int, input().split()) # N nodes, M edges
    u_nodes = list(map(int, input().split())) if M > 0 else []
    v_nodes = list(map(int, input().split())) if M > 0 else []

    # 1. Build Adjacency List (Undirected)
    adj = [[] for _ in range(N + 1)] # List index corresponds to node number (1 to N)
    for i in range(M):
        u, v = u_nodes[i], v_nodes[i]
        adj[u].append(v)
        adj[v].append(u) # Add edge in both directions

    # 2. Initialize Colors and State
    # color[i] = 0 means node i is uncolored (White)
    # color[i] = 1 means node i is Color 'A'
    # color[i] = 2 means node i is Color 'B'
    color = [0] * (N + 1)
    is_bipartite = True  # Assume it's possible until proven otherwise

    # 3. Iterate through all nodes (handles disconnected graphs)
    for start_node in range(1, N + 1):
        # If we already found it's not bipartite, no need to continue
        if not is_bipartite:
            break

        # If this node hasn't been colored yet, start a BFS from here
        if color[start_node] == 0:
            queue = deque()
            color[start_node] = 1  # Start coloring with 'A'
            queue.append(start_node)

            # --- BFS Loop for this component ---
            while queue:
                u = queue.popleft() # Get node from front of queue
                current_node_color = color[u]
                # Determine the color neighbors should have
                neighbor_color = 2 if current_node_color == 1 else 1

                # Look at all neighbors 'v' of node 'u'
                for v in adj[u]:
                    if color[v] == 0: # If neighbor 'v' is uncolored
                        color[v] = neighbor_color # Assign the required color
                        queue.append(v)          # Add it to the queue to process later
                    elif color[v] == current_node_color: # If neighbor 'v' has the SAME color as 'u'
                        # Conflict found! This edge connects two nodes of the same color.
                        is_bipartite = False
                        break # Exit the inner neighbor loop

                # If a conflict was found in the neighbor loop, exit the BFS loop too
                if not is_bipartite:
                    break
            # --- End of BFS Loop for this component ---

    # 4. Determine Final Result
    if not is_bipartite:
        return "X"
    else:
        # Construct the output string based on the coloring
        result_coloring = []
        for i in range(1, N + 1):
            # If a node was isolated (never colored), assign default 'A'
            node_final_color = color[i] if color[i] != 0 else 1
            result_coloring.append("A" if node_final_color == 1 else "B")
        return " ".join(result_coloring)

# Get the result from the solve function
final_answer = solve()
# Print the result
print(final_answer)