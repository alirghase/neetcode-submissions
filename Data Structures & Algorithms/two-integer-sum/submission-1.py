class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        indices = {} # val:index

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in indices.keys():
                return [indices[difference], i]
            else:
                indices[nums[i]] = i
