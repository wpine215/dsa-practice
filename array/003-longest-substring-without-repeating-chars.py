# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Demonstrates sliding window technique

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        i_left = 0
        i_right = 0
        current_max = 0
        
        while i_right < len(s):
            if s[i_right] in seen and seen[s[i_right]] >= i_left:
                # Repeating character found in current sliding window, move left past previous occurence
                i_left = seen[s[i_right]] + 1
            else:
                # No duplicates found in this iteration, update seen & extend right window cursor by 1
                seen[s[i_right]] = i_right
                i_right += 1
                current_max = max(current_max, i_right - i_left)
        
        return current_max
