"""
6. Zigzag Conversion
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = [[] for _ in range(numRows)]
        n = 0
        for c in enumerate(s):
            if n < numRows:
                result[n].append(c)
                n+=1

