# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        global act
        act = 0
        global k_value
        k_value = -1

        def traverse(root):
            if root:
                traverse(root.left)
                global act
                global k_value
                if k_value == -1:
                    act += 1
                    if act == k:
                        k_value = root.val
                traverse(root.right)

        traverse(root)
        return k_value