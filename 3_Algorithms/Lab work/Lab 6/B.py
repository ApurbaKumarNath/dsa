'''
There is an intense football match going on between Robots and Humans. However, things aren't as simple as they seem — 
the Robots have disguised themselves to look exactly like Humans! From the outside, it's impossible to tell who is a Robot and who is a Human.

The audience know only one important information — the Robots tackles only the Humans, and the Humans tackles only the Robots.

Now, you are given a list of tackles, each involving two players. Based on this information, find the maximum possible number of Robots or Humans.

5 6
3 4
3 2
5 4
5 2
4 1
1 2

3
'''

from collections import deque

def solve():
    N, M = map(int, input().split())

    # Initialization (using list of lists)__________________________________
    adj = [[] for _ in range(N + 1)] # Adjacency list (list of lists)
    color = [0] * (N + 1)           # 0: unvisited, 1: Team 1, 2: Team 2
    total_max_players = 0

    # Build Adjacency List (Undirected)____________________________________
    for _ in range(M):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u) # Add edge in both directions

    # BFS for each component: checks bipartiteness implicitly & counts teams_
    for i in range(1, N + 1):
        if color[i] == 0: # Found an unvisited node, start BFS for its component
            
            q = deque()
            q.append(i)
            color[i] = 1 # Start assigning to Team 1

            # Count nodes in each potential team for THIS component
            count1 = 0
            count2 = 0
            
            # Component BFS Loop________________________________________________
            while q:
                u = q.popleft()

                # Assign to team based on color and increment count
                if color[u] == 1:
                    count1 += 1
                    neighbor_color = 2
                else: # color[u] == 2
                    count2 += 1
                    neighbor_color = 1

                # Process neighbors
                for v in adj[u]:
                    if color[v] == 0: # If neighbor is unvisited
                        color[v] = neighbor_color
                        q.append(v)
                    # Implicit check: If color[v] was already set BUT is the same
                    # as color[u], the graph isn't bipartite. However, the problem
                    # asks for max *possible*, implying we assume it *is* possible.
                    # So, we don't need an explicit error check here.

            # Add the max team size from this component to the total__________
            total_max_players += max(count1, count2)

    # Return total maximum_________________________________________________
    return total_max_players

# Main execution______________________________________________________________
output = solve()
print(output)