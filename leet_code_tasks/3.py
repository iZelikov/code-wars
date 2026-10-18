class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = -1
        r = 0
        longest_substring = 0
        chars = set()
        while r < len(s):
            if s[r] in chars:
                l += 1
                chars.remove(s[l])
            else:
                chars.add(s[r])
                longest_substring = max(longest_substring, r - l)
                r += 1
        return longest_substring

print(Solution().lengthOfLongestSubstring("bbbbb"))
