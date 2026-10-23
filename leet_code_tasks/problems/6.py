"""
6. Zigzag Conversion
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = [[] for _ in range(numRows)]
        period = 2 * numRows - 2
        for i, c in enumerate(s):
            j = min(i % period, period - i % period)
            result[j].append(c)
        rs = ''.join(''.join(x) for x in result)
        return rs

print(Solution().convert("a",1))