# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        arr = []
            
        def traverse(root):
            if root == None:
                return
            
            if root.left != None:
                traverse(root.left)
                
            arr.append(root.val)
            
            if root.right != None:
                traverse(root.right)
        
        traverse(root)
        
        return arr

        