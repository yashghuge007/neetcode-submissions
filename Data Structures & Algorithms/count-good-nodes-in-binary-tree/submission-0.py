# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, currmax):
            if not root:
                return 0
            
            res = 0 if root.val<currmax else 1
            currmax = max(root.val,currmax)

            res+= dfs(root.left,currmax)
            res+= dfs(root.right,currmax)

            return res
        return dfs(root,root.val)