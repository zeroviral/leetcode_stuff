# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        graph = collections.defaultdict(set)
        def dfs(node):
            if node:
                if node.left:
                    graph[node.val].add(node.left.val)
                    graph[node.left.val].add(node.val)
                    
                if node.right:
                    graph[node.val].add(node.right.val)
                    graph[node.right.val].add(node.val)
                
                dfs(node.left)
                dfs(node.right)
                
        dfs(root)
        
        queue = [(target.val,0)]
        visited = set([target.val])
        res = []
        while queue:
            size = len(queue)
            for i in range(size):
                current,length = queue.pop(0)
                if length == K:
                    res.append(current)
                for v in graph[current]:
                    if v not in visited:
                        visited.add(v)
                        queue.append((v,length+1))
                
        return res