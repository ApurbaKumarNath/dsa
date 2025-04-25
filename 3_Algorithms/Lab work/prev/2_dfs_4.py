'''
You are given an undirected and unweighted graph with N cities and N-1 roads. Every city has a value, P, which denotes the amount of Gold 
you can get if you visit the city. You can collect the gold only once.
You are starting your journey from city 1. Now, you have to find a city, T, such that, if you visit from city 1 to T, 
you can collect the maximum amount of gold.

21:
7 6
5 10 2 3 6 10 7
1 2
1 5
2 3
2 4
5 6
5 7
'''

# No need for color array in tree DFS if we pass the parent
# d[] array isn't needed directly, we calculate path sums on the fly

def dfs(u, parent, gold_sum_to_parent, adj, gold_values, max_info):
    """
    Performs DFS to find the max gold path starting from node 1.

    Args:
        u: The current city being visited.
        parent: The city from which we arrived at u (to avoid going back).
        gold_sum_to_parent: The accumulated gold on the path from city 1 up to the parent city.
        adj: The adjacency list representing the roads.
        gold_values: List containing gold amount for each city (P, 1-indexed).
        max_info: A list [max_gold_found, target_city] used to store the overall maximum.
                  This list is modified directly (acts like passing by reference).
    """
    # Calculate the total gold collected on the path ending at the current city 'u'
    gold_sum_at_u = gold_sum_to_parent + gold_values[u]

    # Update max_info if the path ending at 'u' has more gold
    if gold_sum_at_u > max_info[0]:
        max_info[0] = gold_sum_at_u  # Update max gold found
        max_info[1] = u              # Update the target city

    # --- Explore neighbors ---
    for v in adj[u]:
        # Only proceed to a neighbor 'v' if it's not the parent we just came from
        if v != parent:
            # Recursive call for the neighbor 'v':
            # - 'u' becomes the parent for the next step.
            # - Pass the gold sum accumulated *up to u* (gold_sum_at_u)
            #   as the 'sum_to_parent' for the next call.
            dfs(v, u, gold_sum_at_u, adj, gold_values, max_info)


def solve():
    N, M = map(int, input().split())

    gold_input = list(map(int, input().split()))
    # Create a 1-indexed list P. P[0] is unused.
    P = [0] + gold_input

    # --- 3. Build Adjacency List (Undirected) ---
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    # Handle edge case of no cities (though constraints likely prevent N<1)
    if N < 1:
         return [-1, -float('inf')] # Return invalid city and negative infinity gold

    # max_info = [max_gold_found, target_city]
    # Initialize with the path consisting of only the start node (City 1)
    # The initial maximum gold is just the gold in City 1.
    max_info = [P[1], 1]

    # --- 5. Start DFS from City 1 ---
    start_node = 1
    parent_of_start = 0 # Use 0 to indicate no parent for the root
    gold_sum_before_start = 0 # Gold accumulated *before* reaching node 1 is 0

    # Initial DFS call. The function will handle adding P[1] internally.
    dfs(start_node, parent_of_start, gold_sum_before_start, adj, P, max_info)

    # --- 6. Return Result ---
    # Return the target city and the maximum gold found: [target_city, max_gold_found]
    return [max_info[1], max_info[0]]


result = solve()
print(result)
# Expected output for Example 1: [6, 21]
# Expected output for Example 2: [6, 5]