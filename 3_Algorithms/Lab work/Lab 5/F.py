from collections import deque

R, H = map(int, input().split()) # R= rows, H=columns
grid = [input().strip() for _ in range(R)] # Read grid row by row

color = [[0 for _ in range(H)] for _ in range(R)] # 0: unvisited/white, 1: visited/Gray
max_diamonds = 0

dr = [-1, 1, 0, 0] # row direction
dc = [0, 0, -1, 1] # column direction
# i for dr and dc; 0: up, 1: down, 2: left, 3: right

#BFS initialization with outer loop for unconnected components__________________________________

for r in range(R):
    for c in range(H):
        if grid[r][c] != '#' and color[r][c] == 0: # if unvisited and not a wall
            color[r][c] = 1

            curr_diamonds = 0
            if grid[r][c] == 'D':
                curr_diamonds += 1

            queue = deque() # Start BFS
            queue.append((r, c)) # Enqueue the starting cell

            #BFS loop_____________________________________________________________________________________

            while queue:
                ur, uc = queue.popleft() # Dequeue the first element

                for i in range(4): # Check all 4 directions (up, down, left, right); checking adjacents of u (ur, uc)
                    vr = ur + dr[i]
                    vc = uc + dc[i]

                    if 0 <= vr < R and 0 <= vc < H: # Check if within bounds
                        if grid[vr][vc] != '#' and color[vr][vc] == 0: # if unvisited and not a wall

                            color[vr][vc] = 1
                            if grid[vr][vc] == 'D':
                                curr_diamonds += 1
                            queue.append((vr, vc))

            # Update the maximum number of diamonds found in this component________________________________
            max_diamonds = max(max_diamonds, curr_diamonds)
print(max_diamonds)
