class Solution(object):
    def get_sign(self, arr):
        product = 1
        for x in arr:
            product *= x
        return product

    def get_max_product(self, start, end, direct, arr):
        if len(arr) == 1:
            return arr[0]
        
        product = self.get_sign(arr)
        if product > 0:
            return product

        for i in range(start, end, direct):
            product //= arr[i]
            if product > 0 :
                return product
                
        return 0         
        
    def maxProduct(self, nums):
        subarrs = []
        add_arr = []
        has_zero = False
        for x in nums:
            if x == 0:
                has_zero = True
                if len(add_arr) != 0:
                    subarrs.append(add_arr)
                    add_arr = []
                continue

            add_arr.append(x)

        if len(add_arr) != 0:
            subarrs.append(add_arr)

        product = min(nums) if not has_zero else 0

        for subar in subarrs:
            x = self.get_max_product(0, len(subar), 1, subar)
            y = self.get_max_product(len(subar) - 1, -1, -1, subar)
            product = max(product, x, y)

        return product
        