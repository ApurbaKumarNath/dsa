'''
In this problem, there are N courses in the curriculum and M requirements of the form "Course A has to be completed before course B".

Your task is to find an order in which you can complete the courses. If there are multiple valid order, you may print any of them. 
If no such sequence exists, then print −1.

5 4
2 4
2 5
4 3
1 5

2 4 3 1 5
'''

import sys
sys.setrecursionlimit(2*10**5 + 10)

# Global variables for DFS
adj = [] # Adjacency list (will be list of lists)
color = [] # 0: white, 1: gray, 2: black
result = [] # Stores the topological sort (in reverse)
possible = True # Flag to track if a cycle is detected

# Depth First Search function_________________________________________________
def dfs(u):
    global possible
    if not possible: # If cycle already detected elsewhere, stop
        return

    color[u] = 1 # Mark node as visiting (Gray)

    # Iterate through neighbors using the list of lists
    for v in adj[u]:
        if color[v] == 1: # Neighbor is Gray -> Cycle detected
            possible = False
            return
        elif color[v] == 0: # Neighbor is White -> Visit it
            dfs(v)
            if not possible: # Propagate cycle detection signal
                return
        # If color[v] == 2 (Black), do nothing, already processed.

    color[u] = 2 # Mark node as finished (Black)
    result.append(u) # Add to the end of the result list

# Main solve function_________________________________________________________
def solve():
    global possible, color, result, adj
    N, M = map(int, input().split())

    # Initialize adjacency list as a list of lists
    adj = [[] for _ in range(N + 1)] # N+1 empty lists for 1-based indexing

    # Reset other global state
    result = []
    possible = True
    color = [0] * (N + 1) # Use 1-based indexing

    # Build adjacency list____________________________________________________
    for _ in range(M):
        u, v = map(int, input().split())
        adj[u].append(v) # Edge u -> v means u must come before v

    # Perform DFS starting from each unvisited node___________________________
    for i in range(1, N + 1):
        if color[i] == 0: # If node is White
            dfs(i)
        if not possible: # If cycle found during DFS, stop early
            break

    # Check result and return_________________________________________________
    if not possible:
        return "-1"
    else:
        # The result list is in reverse topological order
        result.reverse()
        return " ".join(map(str, result))

# Main execution______________________________________________________________
output = solve()
print(output)