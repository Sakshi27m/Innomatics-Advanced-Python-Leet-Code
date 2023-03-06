class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = max2 = float('-inf') # set max1 and max2 to negative infinity
        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num
        return (max1 - 1) * (max2 - 1) # return the product of the two largest numbers minus 1
