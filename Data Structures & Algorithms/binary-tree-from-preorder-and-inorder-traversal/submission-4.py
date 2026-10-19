class Solution:
    def buildTree(
        self,
        preorder: List[int],
        inorder: List[int]
    ) -> Optional[TreeNode]:

        positions = {
            value: idx
            for idx, value in enumerate(inorder)
        }
        pre_idx = 0

        def dfs(left, right):
            nonlocal pre_idx

            if left >= right:
                return None

            # preorder에서 아직 사용하지 않은 첫 값이 현재 루트
            value = preorder[pre_idx]
            pre_idx += 1

            mid = positions[value]
            node = TreeNode(value)

            node.left = dfs(left, mid)
            node.right = dfs(mid + 1, right)

            return node

        return dfs(0, len(inorder))