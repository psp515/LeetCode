"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        if root == None:
            return []
        
        arr = []
        stack = [ root ]
        
        while stack:
            x = stack.pop()
            arr.append(x.val)
            for c in reversed(x.children):
                if c != None:
                    stack.append(c)
        
        return arr
        
        
        