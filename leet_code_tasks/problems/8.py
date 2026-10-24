"""
8. String to Integer (atoi)
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        max_int = 2 ** 31 - 1
        min_int = -(2 ** 31)
        negative = False
        i = 0
        n = len(s)
        result = []
        while i < n - 1 and s[i] == ' ':
            i += 1
        if s[i] == '-':
            negative = True
            i += 1
        elif s[i] == '+':
            i += 1
        while i < n:
            x = ord(s[i])
            if 47 < x < 58:
                result.append(x - 48)
                i += 1
            else:
                break
        if not result:
            return 0
        int_result = sum(x * 10 ** j for j, x in enumerate(reversed(result)))
        int_result = -int_result if negative else int_result
        int_result = min(max(min_int, int_result), max_int)
        return int_result


print(Solution().myAtoi('   '))
