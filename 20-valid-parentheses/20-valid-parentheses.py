class Solution(object):
    def _match(self, item, arr):
        return any(x == item for x in arr)
    
    def isValid(self, s):
        stack = []
        
        for element in s:
            if self._match(element, ["[", "{", "("]):
                stack.append(element)
            else:
                if len(stack) == 0:
                    return False
                
                data = stack.pop()
                
                if data =="(" and element != ")":
                    return False
                
                if data =="{" and element != "}":
                    return False
                
                if data =="[" and element != "]":
                    return False
        
        return True if len(stack) == 0 else False
            
        