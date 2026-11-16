class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # sorting 

        while len(stones) > 1: 
            stones.sort()
            cur = stones.pop() - stones.pop()
            if cur: 
                stones.append(cur)

        if stones: 
            return stones[0]
        else: 
            return 0