import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_elements = {}

        for num in nums: 
            if num in frequent_elements: 
                frequent_elements[num] += 1
            else:
                frequent_elements[num] = 1

        min_heap = []

        for num, freq in frequent_elements.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [num for freq, num in min_heap]