# https://leetcode.com/problems/k-closest-points-to-origin/

import heapq
import math

class Solution:
    @staticmethod
    def dist_to_origin(x, y):
        return math.sqrt(x**2 + y**2)
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for x, y in points:
            if len(h) < k:
                # We want a max heap (not a min heap), so multiply heapq sort key (first item in iterable) by -1
                heapq.heappush(h, (-1 * Solution.dist_to_origin(x, y), x, y))
            elif (-1 *Solution.dist_to_origin(x, y)) > h[0][0]:
                # If the distance from the current (x,y) is less than the distance of the current top of max heap (taking the negative into account),
                # pop the top of the max heap and push the current (x,y).
                # This ensures that at the end of iteration, the k closest elements are in the heap
                heapq.heappushpop(h, (-1 * Solution.dist_to_origin(x, y), x, y))
        
        # Since the first element in heap tuple was distance, only return the coordinates. Order does not matter.
        return [x[1:] for x in h]
