# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        data = [[0, 0]]
        
        stack = deque([(root, 0)])
        
        while stack:
            r, lvl = stack.popleft()
            
            if len(data) <= lvl:
                data.append([0, 0])
            
            data[lvl][0] += r.val    
            data[lvl][1] += 1
            
            if r.right != None:
                stack.append((r.right, lvl+1))
            
            if r.left != None:
                stack.append((r.left, lvl+1))
            
        return [float(x) / float(y) for x, y in data]
        