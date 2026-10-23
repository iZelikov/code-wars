"""
7. Reverse Integer
"""

class Solution:
    def reverse(self, x: int) -> int:
        result = str(abs(x))[::-1]
        int_result = int(result)
        if int_result < -(2 ** 31) or int_result > (2 ** 31 - 1):
            int_result = 0
        return -int_result if x < 0 else int_result
