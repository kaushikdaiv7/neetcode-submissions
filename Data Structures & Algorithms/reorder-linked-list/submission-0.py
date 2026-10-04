# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = fast = slow = head

        # find mid point of whole linked list
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second_half = slow.next
        slow.next = None

        # reverse second half
        cur = second_half
        prev = None
        while cur:
            next_ = cur.next
            cur.next = prev
            prev = cur
            cur = next_

        second_half = prev
        cur = head
        first_half = head.next

        # combine both halves as we need
        counter = 1
        while first_half and second_half:
            if counter%2==0:
                cur.next = first_half
                first_half = first_half.next
            else:
                cur.next = second_half
                second_half = second_half.next
            counter += 1
            cur = cur.next

        cur.next = first_half or second_half

                



