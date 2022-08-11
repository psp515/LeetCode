class Solution(object):
    def get_keys(self, digit):
        if digit == "2":
            return ["a", "b", "c"]
        elif digit == "3":
            return ["d", "e", "f"]
        elif digit == "4":
            return ["g", "h", "i"]
        elif digit == "5":
            return ["j", "k", "l"]
        elif digit == "6":
            return ["m", "n", "o"]
        elif digit == "7":
            return ["p", "q", "r", "s"]
        elif digit == "8":
            return ["t", "u", "v"]
        else:
            return ["w", "x", "y", "z"]
    
    
    
    def letterCombinations(self, digits):
        ans = []
        
        for digit in digits:
            arr = self.get_keys(digit)
            if len(ans) == 0:
                for element in arr:
                    ans.append(element)
            else:
                copy = ans
                ans = []
                
                for element in copy:
                    for ele in arr:
                        ans.append(element+ele)
                        
            
        return ans
            
            
        