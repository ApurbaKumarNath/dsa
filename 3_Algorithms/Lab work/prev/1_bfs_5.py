'''
In a small village, Ella the painter loves to add color to old photos. One day, she finds a faded photo represented by a grid, 
where 0 means gray (can't be colored) and 1 means black. Ella starts coloring at a specific point (sr, sc) with her chosen color. 
She can only move diagonally (top-left, top-right, bottom-left, bottom-right) from one cell to another. Starting from the image[sr][sc], 
she spreads her color to any diagonally connected cells that share the same initial color. Ella can color a cell if and only if that 
cell contains black color. Now help Ella by simulating this process: replace the color of all the relevant pixels with her chosen color and 
return the newly colored photo.

input:
1 1 2
3 3
0 1 0
1 1 1
0 1 0

output:
0 1 0
1 2 1
0 1 0
'''
from collections import deque

def solve():
    """
    Performs diagonal flood fill on a grid.

    Reads input, performs the coloring operation, and returns the modified grid.
    """
    # --- 1. Read Input ---
    sr_in, sc_in, new_color = map(int, input().split())
    n, m = map(int, input().split())
    # Read grid, converting rows into lists of integers
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))

    # Use 0-based indexing internally.
    # Adjust if problem specifies 0-based input.
    sr = sr_in
    sc = sc_in

    # --- 2. Check Initial Conditions ---
    # Check if start is out of bounds (after potential adjustment)
    if not (0 <= sr < n and 0 <= sc < m):
        return grid # Return original grid if start is invalid

    original_color = grid[sr][sc]

    # If starting cell cannot be colored (is gray) or already has the new color
    if original_color == 0 or original_color == new_color:
        return grid # Return the original grid, no changes needed

    # --- 3. Initialize BFS ---
    queue = deque()
    # Define diagonal movements (dr = delta row, dc = delta column)
    dr = [-1, -1, 1, 1]
    dc = [-1, 1, -1, 1]

    # --- 4. Start BFS ---
    grid[sr][sc] = new_color # Color the starting cell
    queue.append((sr, sc))   # Add it to the queue

    while queue:
        r, c = queue.popleft()

        # Explore diagonal neighbors
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            # Check bounds
            if 0 <= nr < n and 0 <= nc < m:
                # Check if neighbor has the original color
                if grid[nr][nc] == original_color:
                    grid[nr][nc] = new_color # Color the neighbor
                    queue.append((nr, nc))   # Add neighbor to queue

    # --- 5. Return Modified Grid ---
    return grid

# --- Example of how to call the function and print the result ---
if __name__ == "__main__":
    modified_grid = solve()
    for row in modified_grid:
        print(*row) # Print each element separated by space