import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for n in nums:
            if n in freq_map:
                freq_map[n] +=1
            else:
                freq_map[n] = 1
                
        h = []
        for num, occ in freq_map.items():
            heapq.heappush(h, (-1 * occ, num))
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(h)[1])
        
        return res
