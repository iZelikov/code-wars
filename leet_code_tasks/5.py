"""
5. Longest Palindromic Substring
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        for i in range(len(s)):
            d = 0
            while d <= i and d < len(s) - i and s[i - d] == s[i + d]:
                d += 1
            if 2 * d - 1 > len(longest):
                longest = s[i - d + 1: i + d]
            d = 0
            while d <= i and d < len(s) - i - 1 and s[i - d] == s[i + d + 1]:
                d += 1
            if 2 * d > len(longest):
                longest = s[i - d + 1: i + d + 1]

        return longest


print(Solution().longestPalindrome("cbbad"))
