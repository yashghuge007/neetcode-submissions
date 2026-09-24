# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        q = deque()
        q.append(root)
        while q:
            temp = []
            n = len(q)
            for i in range(n):
                r = q.popleft()
                temp.append(r.val)
                if r.left: q.append(r.left)
                if r.right: q.append(r.right)
            ans.append(temp)
        return ans

