# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        if not head:
            return 0

        if not head.next.next:
            return head.val + head.next.val

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse second half of the list

        curr = slow
        prev = None

        while curr:

            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode

        maxsum = 0
        first = head
        second = prev

        while second:
            currsum = first.val + second.val
            maxsum = max(maxsum, currsum)
            first = first.next
            second = second.next

        return maxsum