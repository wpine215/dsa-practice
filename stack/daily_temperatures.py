class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Monotonic stack problem
        stack = []
        days = [0] * len(temperatures)
        
        for i, temp in enumerate(temperatures):
            while len(stack) > 0 and temp > stack[-1][0]:
                _, p_i = stack.pop()
                days[p_i] = i - p_i
            stack.append((temp, i))
        
        return days
