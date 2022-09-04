# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        values = []
        def traverse(root):
            if root:
                traverse(root.left)
                values.append(root.val)
                traverse(root.right)
        
        traverse(root)
        mini = float('inf')

        for i in range(1, len(values)):
            mini = min(mini, abs(values[i] - values[i-1]))
          
        return mini
        