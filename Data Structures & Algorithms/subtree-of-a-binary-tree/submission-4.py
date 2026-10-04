# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def sameT(self,p,q):
        if not p and not q:
            return True
        if (p and not q) or (q and not p):
            return False
        return p.val==q.val and self.sameT(p.left,q.left) and self.sameT(p.right,q.right)

    def isSubtree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q:
            return True
        if not p:
            return False
        if self.sameT(p,q):
            return True
        return self.isSubtree(p.left,q) or self.isSubtree(p.right,q) 