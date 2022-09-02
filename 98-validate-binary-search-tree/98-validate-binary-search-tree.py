# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def isValidBST(self, root):
        stack = [(root, float('-inf'), float('inf'))]

        while stack:
            node, l, r = stack.pop()
            
            if node == None or node == node.left or node == node.right:
                continue

            if not (l < node.val < r):
                return False

            stack.append((node.right, node.val, r))
            stack.append((node.left, l, node.val))

        return True