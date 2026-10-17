# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], lb: int, ub: int) -> bool:
            if not node:
                return True

            if node.val == 0:
                print(node.left, node.right, lb, ub)

            if lb > -1 and node.val <= lb:
                return False
            elif ub > -1 and node.val >= ub:
                return False

            left_subtree = dfs(node.left, lb, node.val)
            right_subtree = dfs(node.right, node.val, ub)
            return left_subtree and right_subtree

        return dfs(root, -1, -1)
            
                
        

# 0
# -1000 1000
# x x 0