# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def recursive(currentNode: TreeNode, currentSum: int, targetSum: int) -> bool:
            if currentNode is None:
                return False
            elif currentNode.left is None and currentNode.right is None:
                return currentSum + currentNode.val == targetSum
            else:
                leftResult = recursive(
                    currentNode.left, currentSum + currentNode.val, targetSum)
                rightResult = recursive(
                    currentNode.right, currentSum + currentNode.val, targetSum)
                return leftResult or rightResult
        return recursive(root, 0, targetSum)
        