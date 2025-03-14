def find_postorder(inorder, preorder):
    inorder_map = {} # mapping of value to index for inorder
    for i in range(len(inorder)):
        inorder_map[inorder[i]] = i
    
    postorder = []
    
    def build_postorder(pre_start, pre_end, in_start, in_end):
        if pre_start > pre_end or in_start > in_end:
            return
        
        root_val = preorder[pre_start] # 1st elem in preorder is root
        
        root_inorder_idx = inorder_map[root_val] # Find position of root in inorder
        
        left_size = root_inorder_idx - in_start # Calculate size of left subtree
        
        build_postorder(pre_start + 1, pre_start + left_size, in_start, root_inorder_idx - 1)
        build_postorder(pre_start + left_size + 1, pre_end, root_inorder_idx + 1, in_end)
        
        
        postorder.append(root_val) # Add root to postorder (visit after both subtrees)
    
    build_postorder(0, len(preorder) - 1, 0, len(inorder) - 1)
    return postorder


n = int(input())
inorder = list(map(int, input().split()))
preorder = list(map(int, input().split()))

postorder = find_postorder(inorder, preorder)

print(" ".join(map(str, postorder)))