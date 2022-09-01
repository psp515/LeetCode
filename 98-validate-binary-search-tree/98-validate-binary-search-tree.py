# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        if not root:
            return True
        return self.isValidNode(root,float('-inf'), float('inf'))
    
    def isValidNode(self, root, l, r):
        if not root:
            return True
        return l < root.val < r and self.isValidNode(root.left, l, root.val) and self.isValidNode(root.right, root.val, r)
            