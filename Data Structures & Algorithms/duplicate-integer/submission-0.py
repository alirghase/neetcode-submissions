class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenNumbers = set()

        for currentNum in nums:
            if currentNum in seenNumbers:
                return True
            else:
                seenNumbers.add(currentNum)
        return False