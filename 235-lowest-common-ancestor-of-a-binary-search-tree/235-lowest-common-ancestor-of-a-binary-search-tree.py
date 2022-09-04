# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        p, q = sorted([p.val, q.val])
        while not p <= root.val <= q:
            root = (root.left, root.right)[p > root.val]
        return root
        