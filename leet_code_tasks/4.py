"""
4. Median of Two Sorted Arrays
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        n, m = len(nums1), len(nums2)
        if n > m:
            nums1, nums2 = nums2, nums1
            n, m = m, n
        half = (n + m + 1) // 2
        NEG, POS = float('-inf'), float('inf')
        l, r = 0, n
        while l <= r:
            i = (l + r) // 2
            j = half - i
            a_left = nums1[i - 1] if i > 0 else NEG
            a_right = nums1[i] if i < n else POS
            b_left = nums2[j - 1] if j > 0 else NEG
            b_right = nums2[j] if j < m else POS
            if a_left > b_right:
                r = i - 1
            elif b_left > a_right:
                l = i + 1
            else:
                if (n + m) % 2:
                    return a_left if a_left > b_left else b_left
                lo = a_left if a_left > b_left else b_left
                hi = a_right if a_right < b_right else b_right
                return (lo + hi) / 2


print(Solution().findMedianSortedArrays([5], []))
