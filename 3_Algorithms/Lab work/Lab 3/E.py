def ordering_tree(arr):
    result = []
    
    def build_bst(start, end):
        if start > end:
            return
        
        mid = (start + end) // 2
        
        result.append(arr[mid])
        
        build_bst(start, mid - 1)
        
        build_bst(mid + 1, end)
    
    build_bst(0, len(arr) - 1)
    
    return result


n = int(input())
A = list(map(int, input().split()))

optimal_order = ordering_tree(A)

print(" ".join(map(str, optimal_order)))