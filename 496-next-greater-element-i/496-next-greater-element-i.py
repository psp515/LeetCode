class Solution(object):
    def nextGreaterElement(self, arr1, arr2):
        n,m = len(arr1), len(arr2)
        returnable = []
        for i in range(n):
            addable = -1
            found_j = False
            for j in range(m):
                if arr1[i] == arr2[j]:
                    found_j = True
                
                if found_j and arr1[i] < arr2[j]:
                    addable = arr2[j]
                    break
            returnable.append(addable)

        return returnable 
        