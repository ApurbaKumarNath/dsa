from collections import deque
def solve():
    n, m, s, dn = map(int, input().split()) # n = no. of vertices, m = no. of edges, s = start node, dn = destination node

    if s == dn:
        print(0); print(s) # edge case
        if m > 0:
            u_nodes = input()
            v_nodes = input()
        return

    u_nodes = list(map(int, input().split())) if m > 0 else []
    v_nodes = list(map(int, input().split())) if m > 0 else []

    #adj list_____________________________________________________________________________________

    adj = [[] for _ in range(n + 1)] # 1-indexed adjacency list as 1st vertex is 1

    for i in range(m): # Read m edges (u, v each) and build the adj. list
        u = u_nodes[i]; v = v_nodes[i]
        adj[u].append(v); adj[v].append(u)

    for i in range(1, n + 1):
        adj[i].sort() # Sort the adjacency list for consistent traversal order

    #initialize BFS_____________________________________________________________________________________

    color = [0] * (n + 1) # All vertices are initially white; 0: unvisited/white, 1: visited/Gray; 1-indexed
    color[s] = 1 # Mark the start node as Gray

    parent = [-1] * (n + 1) # To store the parent of each node

    d = [-1] * (n + 1) # To store the distance from the start node
    d[s] = 0 # Distance from start node to itself is 0

    found = False # Flag to check if the destination node is found

    queue = deque() # Initialize the queue
    queue.append(s) # initially add the start node to the queue

    #BFS loop_____________________________________________________________________________________

    while queue:
        u = queue.popleft() 

        if u == dn: # If the destination node is found
            found = True
            break

        for v in adj[u]: 
            if color[v] == 0: # if color is white (unvisited)
                color[v] = 1  # Mark the neighbor as Gray
                parent[v] = u
                d[v] = d[u] + 1
                queue.append(v)

    #output_____________________________________________________________________________________

    if not found:
        print(-1)
    else:
        print(d[dn]) # Print the distance from start node to destination node

        path = []
        curr = dn
        while curr != -1:
            path.append(curr)
            curr = parent[curr]
        
        path.reverse() # Reverse the path to get the correct order
        print(" ".join(map(str, path))) # Print the path from start node to destination node

solve()
