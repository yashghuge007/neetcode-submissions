# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        ans = []
        q.append(root)
        while q:
            ql = len(q)
            temp = None

            for i in range(ql):
                node = q.popleft()
                if node:
                    temp = node
                    q.append(node.left)
                    q.append(node.right)
            if temp:
                ans.append(temp.val)
        return ans