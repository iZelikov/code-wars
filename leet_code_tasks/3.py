"""
3. Longest Substring Without Repeating Character
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = -1
        r = 0
        len_s = len(s)
        longest_substring = 0
        chars = set()
        while r < len_s:
            if s[r] in chars:
                l += 1
                chars.remove(s[l])
            else:
                chars.add(s[r])
                longest_substring = max(longest_substring, r - l)
                r += 1
        return longest_substring

print(Solution().lengthOfLongestSubstring("bbbbb"))
