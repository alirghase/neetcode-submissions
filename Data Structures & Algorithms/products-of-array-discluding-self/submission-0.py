class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # compute left products
        left = 1
        for i in range(n):
            output[i] = left
            left = nums[i] * left
        
        right = 1
        for i in range(n-1, -1, -1):
            output[i] *= right
            right = nums[i] * right
        
        return output