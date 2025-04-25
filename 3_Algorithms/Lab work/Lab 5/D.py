'''
Through the Jungle
You are given a directed unweighted graph with N nodes and M edges. The nodes are numbered from 1 to N. The graph contains no self-loops or multiple edges.
You have to find a shortest path from node S to node D that passes through node K. If multiple such paths exist, print any one of them. 
If no such path exists, print −1.
'''


from collections import deque
def solve():
    N, M, S, D, K = map(int, input().split()) # N = no. of vertices, M = no. of edges, S = start node, D = destination node, K = one node between S and D

    #adj list_____________________________________________________________________________________

    adj = [[] for _ in range(N + 1)] # 1-indexed adj. list (1st vertex = 1); directed graph
    for _ in range(M):
        u, v = map(int, input().split())
        adj[u].append(v)

    #output_____________________________________________________________________________________

    dsk, psk = bfs(S, K, adj, N)
    if dsk == -1:
        print(-1)
        return
    dkd, pkd = bfs(K, D, adj, N) 
    if dkd == -1:
        print(-1)
        return
    
    print(dsk + dkd)
    print(' '.join(map(str, psk + pkd[1:]))) # print the path from S to K and from K to D, excluding K in the second part of the path

#initialize BFS_____________________________________________________________________________________

def bfs(S, D, adj, N):
    if S == D:
        return 0, [S] # edge case
    
    color = [0] * (N + 1)
    color[S] = 1

    parent = [-1] * (N + 1)

    d = [-1] * (N + 1)
    d[S] = 0

    found = False

    queue = deque()
    queue.append(S)

    #BFS loop_____________________________________________________________________________________

    while queue:
        u = queue.popleft() 

        for v in adj[u]: 
            if color[v] == 0:
                color[v] = 1
                parent[v] = u
                d[v] = d[u] + 1
                queue.append(v)

                if v == D:
                    found = True
                    break

    if not found:
        return -1, -1
    
    #path reconstruction_____________________________________________________________________________________

    path = []
    curr = D
    
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
    path.reverse()

    return d[D], path # returns the distance from S to D and the path from S to D

solve()
