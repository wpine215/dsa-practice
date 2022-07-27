import bisect

# https://leetcode.com/problems/kth-largest-element-in-a-stream/

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.list = sorted(nums)

    def add(self, val: int) -> int:
        bisect.insort(self.list, val)
        return self.list[(-1 * self.k)]
