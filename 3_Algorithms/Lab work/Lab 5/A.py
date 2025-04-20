from collections import deque

n, m = map(int, input().split())
adj_list = [[] for _ in range(n + 1)] # 1-indexed adjacency list

for _ in range(m): # Read m edges (u, v each) and build the adj. list
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

traversal_order = []
start_node = 1

color = [0] * (n + 1) # All vertices are initially white; 0: unvisited/white, 1: visited/Gray; 1-indexed
color[start_node] = 1 # Mark the start node as Gray


queue = deque() 
queue.append(start_node) # initially add the start node to the queue


while queue:
    u = queue.popleft() # Dequeue the first element
    traversal_order.append(u) # Append the first element to the traversal order

    for v in adj_list[u]: # For each neighbor of u
        if color[v] == 0:
            color[v] = 1
            queue.append(v)
            # Mark the neighbor as Gray and add it to the queue

print(" ".join(map(str, traversal_order))) # Print the traversal order