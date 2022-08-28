
class Solution(object):
    def maxDepth(self, root):
        if root == None:
            return 0
        stack = [(root, 1)]
        maxi = 1
        while stack:
            x, p = stack.pop()
            maxi = max(maxi,p)
            if x.left != None:
                stack.append((x.left, 1+p))
            
            if x.right != None:
                stack.append((x.right,1+p))
            
        
        
        return maxi
        