"""
2. Add Two Numbers
"""


# Definition for singly-linked list.
class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution():
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = ListNode()
        current = result
        prev = current
        while True:
            if l1 and l2:
                current.val += l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1:
                current.val += l1.val
                l1 = l1.next
            elif l2:
                current.val += l2.val
                l2 = l2.next
            else:
                break
            overlap = current.val // 10
            current.val %= 10
            current.next = ListNode(overlap)
            prev = current
            current = current.next
        if current.val == 0:
            prev.next = None
        return result


test = Solution()
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
x = test.addTwoNumbers(l1, l2)
while x:
    print(x.val)
    x = x.next
