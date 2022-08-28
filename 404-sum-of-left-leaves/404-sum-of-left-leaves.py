# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        sum = 0
        stack = [(root, False)]
        
        while stack:
            r, t = stack.pop()
            
            if t and r.left == None and r.right == None:
                sum += r.val
                continue
            
            if r.left != None:
                stack.append((r.left,True))
            
            if r.right != None:
                stack.append((r.right,False))
        
        return sum
            
        