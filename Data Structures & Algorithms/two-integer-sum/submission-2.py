class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sums = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in sums:
                return [sums[difference], i]
            else:
                sums[nums[i]] = i