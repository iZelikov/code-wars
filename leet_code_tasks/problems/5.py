class Solution:
    def longestPalindrome(self, s: str) -> str:
        mod_s = "#" + "#".join(s) + "#"
        n = len(mod_s)
        p = [0] * n
        l, r = 0, -1
        max_d, max_i = 1, 0

        for i in range(n):
            if i <= r:
                mirror = l + r - i
                d = min(p[mirror], r - i + 1)
            else:
                d = 0

            while i - d >= 0 and i + d < n and mod_s[i - d] == mod_s[i + d]:
                d += 1

            p[i] = d

            if i + d - 1 > r:
                l = i - d + 1
                r = i + d - 1

            if d > max_d:
                max_d, max_i = d, i

        return mod_s[max_i - max_d + 2 : max_i + max_d : 2]


print(Solution().longestPalindrome("cbcdcbedcbc"))