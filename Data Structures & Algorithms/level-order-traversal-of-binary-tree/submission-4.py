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
            q2 = deque()
            n = len(q)
            i = 0
            for i in range(n):
                r = q.popleft()
                temp.append(r.val)
                if r.left: q2.append(r.left)
                if r.right: q2.append(r.right)
            ans.append(temp)
            q = q2
        return ans

