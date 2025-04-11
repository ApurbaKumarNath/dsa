n, m = map(int, input().split())
u_nodes, v_nodes = list(map(int, input().split())), list(map(int, input().split()))

in_degrees = [0] * (n + 1) # 1-based indexing
out_degrees = [0] * (n + 1)

for i in range(m):
    out_degrees[u_nodes[i]] += 1
    in_degrees[v_nodes[i]] += 1 # directed graph

for i in range(1, n + 1):
    print(in_degrees[i] - out_degrees[i], end = ' ') # difference of in and out degrees of every node