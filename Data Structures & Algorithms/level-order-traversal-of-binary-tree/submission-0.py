# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def acc(self, node: Optional[TreeNode], level: int):
        if node:
            self.ret[level].append(node.val)
            self.acc(node.left, level + 1)
            self.acc(node.right, level + 1)
        

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ret = collections.defaultdict(lambda: [])
        self.acc(root, 0)
        return [e for e in self.ret.values()]
        

