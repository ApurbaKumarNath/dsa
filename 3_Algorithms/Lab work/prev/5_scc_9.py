'''
There is an undirected unweighted graph with N nodes and M edges. The nodes are numbered from 1 to N. The i’th edge of this graph is 
between the i’th node in the second line and the i’th node in the third line, there is no self loop or multi edge. Find the minimum number 
of edges (and any valid set of such edges) that you need to add to this graph such that after the modification all pairs of nodes are 
connected by at least one path. Do everything in O(N+M) time.

2
1 13
10 2
in:
13 12
1 1 1 2 2 2 3 3 7 4 12 11
2 3 4 5 6 7 8 9 1 12 5 10

'''


from collections import deque

def bfs_component(start_node, N, adj, color):
    """ Explores a single connected component using BFS """
    if color[start_node] != 0: # Should not happen if called correctly
        return

    queue = deque()
    queue.append(start_node)
    color[start_node] = 1 # Mark as visited (Gray is enough for BFS)

    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if color[v] == 0: # If neighbor is White (not visited)
                color[v] = 1 # Mark visited
                queue.append(v)
    # No need to mark Black for this problem

def solve():
    N, M = map(int, input().split())

    # Build Adjacency List (Undirected)
    adj = [[] for _ in range(N + 1)]
    u_nodes = list(map(int, input().split())) if M > 0 else []
    v_nodes = list(map(int, input().split())) if M > 0 else []

    for i in range(M):
        u, v = u_nodes[i], v_nodes[i]
        adj[u].append(v)
        adj[v].append(u)

    # Find Connected Components
    color = [0] * (N + 1) # 0=White (not visited), 1=Visited
    component_representatives = []

    for i in range(1, N + 1):
        if color[i] == 0: # Found start of a new component
            component_representatives.append(i)
            bfs_component(i, N, adj, color) # Explore and mark the entire component

    # Calculate results
    num_components = len(component_representatives)
    edges_needed = num_components - 1

    # Prepare the edges to add (connect rep[0] to rep[1], rep[0] to rep[2], ...)
    new_edges_u = []
    new_edges_v = []
    if edges_needed > 0:
        first_rep = component_representatives[0]
        for i in range(1, num_components):
            other_rep = component_representatives[i]
            new_edges_u.append(first_rep)
            new_edges_v.append(other_rep)

    # Return results
    return edges_needed, new_edges_u, new_edges_v

# --- Main execution ---
edges_count, u_list, v_list = solve()

print(edges_count)
# Print the new edges in the required format (each endpoint on its own line)
if edges_count > 0:
    print(*u_list) # Print all 'u' endpoints
    print(*v_list) # Print all 'v' endpoints