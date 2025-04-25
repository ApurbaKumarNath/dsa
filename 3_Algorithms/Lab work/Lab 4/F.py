'''
The King of Königsberg

You are given an N∗N
chessboard and the initial position (x,y) of a King piece. The King can move one step in any of the 8 possible directions: 
Up, Down, Left, Right, Top-left diagonal, Top-right diagonal, Bottom-left diagonal, Bottom-right diagonal.

Your task is to determine the number of valid moves the King can make in one move. A move is valid if it remains inside the board.
'''

n = int(input())
r, c = map(int, input().split()) # rows, columns = king's position; 1-indexed
# The king can move to any of the 8 surrounding squares
relative_moves = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1 ),          ( 0, 1),
    (1, -1 ), ( 1, 0), ( 1, 1)
]

valid_moves = []
for i,j in relative_moves:
    if 1 <= r+i <= n and 1 <= c+j <= n: # checks if the move is within the board
        valid_moves.append((r+i, c+j))

print(len(valid_moves))
for r,c in valid_moves:
    print(r,c)