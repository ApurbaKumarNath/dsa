'''
You have found an old dictionary containing N words. The words are stored in an order that is different from the regular Latin lexicographic order.

Your task is to determine the order of the alphabet that satisfies the lexicographic order of this dictionary. If there are multiple valid orders,
print the lexicographically smallest one. For example, the sequence S1=′′d x i k′′ is lexicographically smaller than the sequence S2=′′d x p a k′.

If no such valid sequence exists, print −1. A valid ordering is not possible if the characters create cyclic dependencies or if a
longer word appears before a shorter word that is a prefix of it.

9
error
tooth
tot
teeth
their
there
thi
tie
hit

oethir
'''

import heapq
from collections import defaultdict

def solve():
    N = int(input())
    words = [input() for _ in range(N)]

    # Initialization_________________________________________________________
    adj = defaultdict(set)        # Adjacency list (char -> set of chars it must precede)
    in_degree = defaultdict(int)  # In-degree count for each character
    present_chars = set()         # Keep track of all unique characters involved

    # Populate present_chars from all words
    for word in words:
        for char in word:
            present_chars.add(char)
            # Initialize in_degree for all present chars to handle isolated chars
            if char not in in_degree:
                in_degree[char] = 0

    # Build Graph & In-degrees from pairwise word comparison_________________
    for i in range(N - 1):
        w1, w2 = words[i], words[i+1]
        min_len = min(len(w1), len(w2))
        diff_found = False
        for j in range(min_len):
            if w1[j] != w2[j]:
                u, v = w1[j], w2[j]
                # Add edge u -> v only if it's not already there
                if v not in adj[u]:
                    adj[u].add(v)
                    in_degree[v] += 1
                diff_found = True
                break # Only the first difference matters

        # Prefix check: If no difference found and w1 is longer than w2
        if not diff_found and len(w1) > len(w2):
            return "-1" # Invalid ordering (e.g., "apple" before "app")

    # Initialize Min-Heap (Priority Queue)_________________________________
    # Add all characters with an in-degree of 0 to the min-heap
    min_heap = [char for char in present_chars if in_degree[char] == 0]
    heapq.heapify(min_heap) # O(V) heapify

    # Process Heap (Kahn's Algorithm with Lexicographical smallest)_________
    result = []
    while min_heap:
        u = heapq.heappop(min_heap) # Get the smallest character with 0 in-degree
        result.append(u)

        # Use a sorted list of neighbors to maintain determinism if needed,
        # but heapq handles the lexicographical choice correctly.
        # Process neighbors in sorted order to break ties consistently if any edge cases existed
        # (though not strictly necessary for correctness here due to heap property)
        sorted_neighbors = sorted(list(adj[u])) # Sort for deterministic tie-breaking if ever needed

        for v in sorted_neighbors: # For each neighbor v of u
            in_degree[v] -= 1
            if in_degree[v] == 0:
                heapq.heappush(min_heap, v) # Add newly free character to heap

    # Check Result___________________________________________________________
    # If the result contains all characters involved, it's a valid sort
    if len(result) == len(present_chars):
        return "".join(result)
    else:
        # Otherwise, there must have been a cycle
        return "-1"

# Main execution______________________________________________________________
output = solve()
print(output)