'''
The Crows have invented a new dictionary of N words. The words are stored in an order which is different from our regular Latin lexicographic order.
Now you have to find the order of the alphabet that satisfies the lexicographic order of the new dictionary. If there are multiple valid orders 
you may print any one of those.
'''


from collections import deque, defaultdict

def solve():
    N = int(input())
    words = [input().strip() for _ in range(N)]

    adj = defaultdict(set)      # Stores graph: char -> {neighbor_chars}
    in_degree = defaultdict(int) # Stores in-degree: char -> count
    chars = set()               # Stores all unique chars present in input

    # --- 1. Build Graph & Find Dependencies ---
    for i in range(N):
        # Add all characters of the current word to the set
        for char in words[i]:
            chars.add(char)
        # Compare with the next word (if it exists)
        if i + 1 < N:
            word1 = words[i]
            word2 = words[i+1]
            min_len = min(len(word1), len(word2))
            diff_found = False

            for j in range(min_len):
                c1, c2 = word1[j], word2[j]
                if c1 != c2:
                    # Found the first difference: c1 must come before c2
                    # Add edge only if it's not already there
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        in_degree[c2] += 1
                        # Ensure c1 is in in_degree map, even if its in-degree is 0
                        in_degree.setdefault(c1, 0)
                    diff_found = True
                    break # Stop comparing this pair once difference is found

            # Check for invalid prefix case (e.g., "apple" before "app")
            if not diff_found and len(word1) > len(word2):
                return "Impossible"

    # --- 2. Initialize Queue for Topological Sort ---
    # Start with nodes having an in-degree of 0
    # Sort alphabetically for deterministic output (though not strictly required by problem)
    queue = deque(sorted([c for c in chars if in_degree[c] == 0]))
    result = []

    # --- 3. Perform Topological Sort ---
    while queue:
        u = queue.popleft()
        result.append(u)

        # Process neighbors (in sorted order for deterministic output)
        # Creating a sorted list to avoid modifying set during iteration
        neighbors = sorted(list(adj[u]))
        for v in neighbors:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
        # Sort the queue after adding new elements to maintain alphabetical processing order
        # This makes the output deterministic but might be slightly less efficient
        queue = deque(sorted(list(queue)))


    # --- 4. Check for Cycles & Return Result ---
    if len(result) == len(chars):
        return " ".join(result)
    else:
        # If lengths don't match, it implies a cycle was present
        return "Impossible"

# --- Run the solver ---
output = solve()
print(output) # Print the returned value from solve()