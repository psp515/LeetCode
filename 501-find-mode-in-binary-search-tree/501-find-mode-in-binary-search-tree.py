# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        
        if root == None:
            return []
        
        d = {}
        stack = [root]
        while stack:
            x = stack.pop()
            value = x.val
            if value in d:
                d[value] += 1
            else:
                d[value] = 1
            
            if x.left != None:
                stack.append(x.left)
            
            if x.right != None:
                stack.append(x.right)
        
        ditems = d.items()
        ditems.sort(reverse=True, key = lambda x:x[1])
        
        ret = [ditems[0][0]]
        
        for i in range(1, len(ditems)):
            if ditems[i][1] == ditems[0][1]:
                ret.append(ditems[i][0])
            else:
                break

        return ret
        
        