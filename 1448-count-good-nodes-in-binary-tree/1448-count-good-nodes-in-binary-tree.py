# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def goodNodes(self, root):
        maxroot = {}
        maxroot[root] = root.val
        stack = deque([(root, -float('inf'))])
        
        while stack:
            x, preval = stack.popleft()
            act = max(preval, x.val)
            maxroot[x] = act
            
            if x.left != None:
                stack.append((x.left, act))
            
            if x.right != None:
                stack.append((x.right, act))
        
        good_count = 0
        
        stack = [root]
        
        while stack:
            x = stack.pop()
            
            if x.val >= maxroot[x]:
                good_count += 1
            
            if x.left != None:
                stack.append(x.left)
            
            if x.right != None:
                stack.append(x.right)
        
        return good_count