# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):    
        stack = [root]
        values = []
        
        while stack:
            x = stack.pop()
            
            values.append(x.val)
            
            if x.left != None:
                stack.append(x.left)
        
            if x.right != None:
                stack.append(x.right)
        
        mini = float('inf')
        values.sort()
        for i in range(1, len(values)):
            mini = min(mini, abs(values[i] - values[i-1]))
        
        
        return mini
            
        