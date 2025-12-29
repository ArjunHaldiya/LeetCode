# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root.left, root.right)

    def isMirror(self, leftNode : Optional[TreeNode] , rightNode: Optional[TreeNode]) -> bool:

        if not leftNode and not rightNode:
            return True

        if not leftNode or not rightNode:
            return False

        if leftNode.val != rightNode.val:
            return False
        
        outerPair = self.isMirror(leftNode.left, rightNode.right)
        innerPair = self.isMirror(leftNode.right, rightNode.left)

        return outerPair and innerPair