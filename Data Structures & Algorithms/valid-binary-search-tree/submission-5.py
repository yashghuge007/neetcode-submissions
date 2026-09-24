# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    minn = float('inf')
    ans = True
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.isValidBST(root.left)
        if self.minn == float('inf'):
             self.minn=root.val
        else:
            if root.val<=self.minn:
                self.ans = False
                return False
            self.minn = root.val
        self.isValidBST(root.right)
        return self.ans
        
        
