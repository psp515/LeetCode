class Solution:
    def myAtoi(self, s: str) -> int:
        is_neg = False
        is_pos = False
        started = False
        data = ""
        n = len(s)
        for i in range(n):
            element = s[i]
            if not started:                  
                if element == " ":
                    continue
                    
                if element == '-':
                    if is_pos:
                        return 0
                    
                    if i + 1 < n:
                        if not s[i+1].isdigit():
                            return 0
                    
                    is_neg = True
                    continue
                    
                if element == "+":
                    if is_neg:
                        return 0
                    
                    if i + 1 < n:
                        if not s[i+1].isdigit():
                            return 0
                    
                    is_pos = True
                    continue
                    
                if element.isdigit():
                    started = True
                    data = data + element
                    continue
                
                break
                
            else:
                if element.isdigit():
                    data = data + element
                else:
                    break
        
        result = 0
        
        if data!="":
            result = int(data)
        
        if is_neg:
            result*=-1
        
        if result > 2147483647:
            return 2147483647
        
        if result < -2147483648:
            return -2147483648
        
        return result