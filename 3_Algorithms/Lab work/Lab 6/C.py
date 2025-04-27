'''
You are given an N×N
 chessboard and the initial position (x1,y1)
 of a Knight piece. You need to find the minimum number of moves the Knight needs to reach the target position (x2,y2). 
 If it is not possible to reach the target, print −1.

3
1 2 1 3

3
'''

from collections import deque

def solve():
    N = int(input())
    x1, y1, x2, y2 = map(int, input().split())

    # Initialization_________________________________________________________
    # Distance array: -1 means unreachable/unvisited
    d = [[-1 for _ in range(N + 1)] for _ in range(N + 1)] # Use 1-based indexing

    # Queue for BFS
    q = deque()

    # Knight move offsets (8 possible moves)
    dx = [-2, -2, -1, -1,  1,  1,  2,  2]
    dy = [-1,  1, -2,  2, -2,  2, -1,  1]

    # Start BFS______________________________________________________________
    if 1 <= x1 <= N and 1 <= y1 <= N: # Check if start is valid
        d[x1][y1] = 0 # Distance from start to start is 0
        q.append((x1, y1)) # Enqueue the starting position

    # BFS Loop_______________________________________________________________
    while q:
        ux, uy = q.popleft() # Get current position

        # If target reached, return distance immediately
        if ux == x2 and uy == y2:
            return d[ux][uy]

        # Explore neighbors (8 possible knight moves)
        for i in range(8):
            vx = ux + dx[i] # Calculate potential next x
            vy = uy + dy[i] # Calculate potential next y

            # Check if the next position (vx, vy) is valid
            # 1. Inside the board bounds (1 to N)
            # 2. Not visited yet (d[vx][vy] == -1)
            if 1 <= vx <= N and 1 <= vy <= N and d[vx][vy] == -1:
                d[vx][vy] = d[ux][uy] + 1 # Update distance
                q.append((vx, vy))       # Enqueue the valid neighbor

    # If queue becomes empty and target wasn't reached_____________________
    return d[x2][y2] # Will be -1 if unreachable

# Main execution______________________________________________________________
output = solve()
print(output)