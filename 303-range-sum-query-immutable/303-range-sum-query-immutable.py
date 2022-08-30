class NumArray(object):

    def __init__(self, arr):
        new_arr = [0 for _ in range(len(arr)+1)]
        for i in range(len(arr)):
            new_arr[i+1] = arr[i] + new_arr[i]
        
        self.arr = new_arr
        

    def sumRange(self, left, right):
        return self.arr[right+1] - self.arr[left]
        
