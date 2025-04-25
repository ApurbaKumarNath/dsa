'''
You are given a maze represented as a 2D grid of size RxH. Each cell in the grid can be an empty space, denoted by '.', a wall 'W', a starting point 'S', or a destination 'D'. There are two players in the jungle, starting from different points, and they aim to reach a single destination point. The objective is to determine which player will reach the destination first. If both players reach the destination at the same time, the result should indicate a tie.

The paths must be the shortest possible in terms of the number of cells traversed. You can only move horizontally or vertically to an adjacent cell.
Player 2:
5 5
2 0
4 0
..w..
.w.w.
..w.D
.w.w.
.....

5 5
0 0
4 0
.....
...w.
..w.D
.w.w.
.....
'''


from collections import deque

def solve():
    # --- Read Grid Size ---
    R, H = map(int, input().split())

    # --- Read Player Start Coordinates ---
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())

    # --- Read Grid ---
    grid = [input().strip() for _ in range(R)]

    # --- Helper BFS function ---
    def bfs(start_r, start_c):
        color = [[0 for _ in range(H)] for _ in range(R)]
        d = [[-1 for _ in range(H)] for _ in range(R)]
        queue = deque()
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        if grid[start_r][start_c] == 'W': return float('inf')

        color[start_r][start_c] = 1
        d[start_r][start_c] = 0
        queue.append((start_r, start_c))

        while queue:
            curr_r, curr_c = queue.popleft()

            # Check if destination reached WHEN DEQUEUED
            if grid[curr_r][curr_c] == 'D':
                return d[curr_r][curr_c] # First time D is popped = shortest path

            for i in range(4):
                next_r, next_c = curr_r + dr[i], curr_c + dc[i]
                if 0 <= next_r < R and 0 <= next_c < H and \
                   grid[next_r][next_c] != 'w' and \
                   color[next_r][next_c] == 0:
                    color[next_r][next_c] = 1
                    d[next_r][next_c] = d[curr_r][curr_c] + 1
                    queue.append((next_r, next_c))
            # No need to mark Black in this version as we return early

        return float('inf') # Destination not reached


    # --- Run BFS for both players ---
    dist1 = bfs(r1, c1)
    dist2 = bfs(r2, c2)

    # --- Compare distances and print result ---
    if dist1 == float('inf') and dist2 == float('inf'):
         return("Error: Neither player can reach destination") # Or handle as per contest rules
    elif dist1 < dist2:
        return("Player 1")
    elif dist2 < dist1:
        return("Player 2")
    else: # dist1 == dist2 (and not both infinity)
        return("Tie")

# Run the solver
print(solve()) 




