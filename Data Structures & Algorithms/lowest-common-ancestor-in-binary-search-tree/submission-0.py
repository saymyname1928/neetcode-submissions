# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def find_node(self, root: TreeNode, target: TreeNode) -> List[TreeNode]:
        print('enter find node')
        cur = root
        ret = [cur]
        while cur.val != target.val:
            if cur.val == target.val:
                ret.append(cur)
                return ret
            elif cur.val < target.val:
                cur = cur.right
                ret.append(cur)
            else:
                cur = cur.left
                ret.append(cur)
        return ret
            

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_anc = self.find_node(root, p)
        q_anc = self.find_node(root, q)

        lca = root
        for p_a, q_a in zip(p_anc, q_anc):
            if p_a.val != q_a.val:
                return lca
            lca = p_a
        return lca
        