# https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for n in nums:
            if len(h) < k:
                # heap hasn't yet reached limiting size of k, so add to it
                heapq.heappush(h, n)
            elif n > h[0]:
                # heap is at max size, so if current number is greater than heap's min number,
                # pop the min number and push the current number.
                # this ensures that at the end of iteration, the top of the min-heap of size k is the kth largest number
                heapq.heappushpop(h, n)
        
        return h[0]
                
