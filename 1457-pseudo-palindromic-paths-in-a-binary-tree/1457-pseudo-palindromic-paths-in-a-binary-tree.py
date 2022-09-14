# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def helper(node):
                if node==None:
                    return
                dict[str(node.val)]+=1
                if node.left==None and node.right==None:                 
                    c=0
                    for i in dict:
                        if dict[i]%2!=0:
                            c+=1
                    if c<=1:
                        ans[0]+=1
                helper(node.left)
                helper(node.right)
                dict[str(node.val)]-=1
        dict=defaultdict(lambda:0)
        ans=[0]
        helper(root)
        return(ans[0])
        