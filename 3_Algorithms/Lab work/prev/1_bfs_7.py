'''The N lines starting from the second line represents a 2D array arr of size N by M such that arr[x][y] = y’th integer in the x’th line. 
There is a grid of size N by M, where the height of the cell at position (x,y) is arr[x][y]. The index numbers in both the array and the grid are 1-based. 
A jump (both way) between two adjacent (up or down or left or right) cells is possible if and only if the absolute difference between their 
heights is less than or equal to K. Find if there is a path from the cell at position (1,1) to the cell at position (N,M), and if there is 
then find any such path. Do everything in O(N*M) time.

3 3 2
1 2 2
3 8 2
5 7 5

(1,1) (2,1) (3,1) (3,2) (3,3)
'''


from collections import deque

def solve():
    # --- 1. Read Input ---
    n, m, k = map(int, input().split())
    # Read grid, store heights as integers
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))

    # --- 2. Initialize ---
    # 0: White (unvisited), 1: Gray (visiting/in queue), 2: Black (visited)
    color = [[0 for _ in range(m)] for _ in range(n)]
    # Store parent coordinates (or None if no parent/start)
    parent = [[None for _ in range(m)] for _ in range(n)]

    # Target coordinates (using 0-based indexing)
    start_r, start_c = 0, 0
    target_r, target_c = n - 1, m - 1

    queue = deque()
    found = False

    # Directions: Up, Down, Left, Right
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # --- 3. Start BFS ---
    if n > 0 and m > 0: # Ensure grid is not empty
        color[start_r][start_c] = 1 # Mark start as Gray
        queue.append((start_r, start_c))
    else:
        return "0" # Handle empty grid case

    while queue:
        curr_r, curr_c = queue.popleft()

        # --- Check if Target Reached ---
        if curr_r == target_r and curr_c == target_c:
            found = True
            break # Exit BFS loop

        # --- Explore Neighbors ---
        for i in range(4):
            next_r, next_c = curr_r + dr[i], curr_c + dc[i]

            # --- Check Validity ---
            # a) Is it within grid bounds?
            if 0 <= next_r < n and 0 <= next_c < m:
                 # Check height difference (absolute value)
                 height_diff = abs(grid[curr_r][curr_c] - grid[next_r][next_c])

                 # b) Is height difference allowed? AND c) Is it unvisited (White)?
                 if height_diff <= k and color[next_r][next_c] == 0:
                     # --- Process Valid Neighbor ---
                     color[next_r][next_c] = 1         # Mark Gray
                     parent[next_r][next_c] = (curr_r, curr_c) # Set parent
                     queue.append((next_r, next_c))    # Add to queue

        # Mark current node as fully processed (Black) - Optional but good practice
        color[curr_r][curr_c] = 2

    # --- 4. Path Reconstruction or Return 0 ---
    if not found:
        return "0"
    else:
        path_coords = []
        curr = (target_r, target_c)
        while curr is not None:
            # Add 1 to convert 0-based index back to 1-based for output format
            path_coords.append(f"({curr[0] + 1},{curr[1] + 1})")
            # Move to the parent cell
            curr = parent[curr[0]][curr[1]]

        # The path is reconstructed backwards, so reverse it
        path_coords.reverse()
        # Join the coordinates into a single space-separated string
        return " ".join(path_coords)

# --- Run the code and print the returned result ---
result = solve()
print(result)