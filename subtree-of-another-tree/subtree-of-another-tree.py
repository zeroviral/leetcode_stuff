# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        def dfs(root):
            
            if not root:
                return "null"
            
            return f"#{dfs(root.left)} + {root.val} + {dfs(root.right)}"
        
        dfs(s)
        ans = dfs(t)
        
        
        string1 = dfs(s)
        string2 = dfs(t)
        
        print(string1, string2)
        
        return string2 in string1
        
        
        
        
            
        
        