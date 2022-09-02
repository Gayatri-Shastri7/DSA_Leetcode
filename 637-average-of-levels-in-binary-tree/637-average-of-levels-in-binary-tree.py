# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        S= defaultdict(float)
        T= defaultdict(float)
        
        def dfs(node,h):
            if not node: return
            dfs(node.left,h+1)
            dfs(node.right,h+1)
            S[h] += node.val
            T[h] += 1
        dfs(root,0)
        

        return(S[i]/T[i] for i in range(len(S)))
'''
Here, we shud find the average heigth of each tree.

'''