'''
The Seven Bridges of Königsberg
You are given an undirected unweighted connected graph with N nodes and M edges. There can be self loop or multiple edges. 
Your task is to determine whether an Eulerian Path exists in the graph.
In graph theory, an Eulerian path (also called an Eulerian trail or Eulerian walk) is a path in a graph that visits every edge exactly 
once and may start and end at different vertices. However, a vertex can be visited multiple times.
'''

n, m = map(int, input().split())
u_nodes, v_nodes = list(map(int, input().split())), list(map(int, input().split()))
degrees = [0] * (n + 1)
for i in range(m):
    degrees[u_nodes[i]] += 1
    degrees[v_nodes[i]] += 1 # undirected graph
odd = 0 # count of odd degree nodes; (eulerian path = 0 or 2) ~ (0 = circuit)
for i in range(1, n + 1):
    if degrees[i] % 2 != 0:
        odd += 1
if odd == 0 or odd == 2:
    print("YES")
else:
    print("NO")