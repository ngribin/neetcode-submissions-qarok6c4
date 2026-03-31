# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        vals = []

        curr = list1

        while curr:
            vals.append(curr.val)
            curr = curr.next


        curr = list2
        while curr:
            vals.append(curr.val)
            curr = curr.next

        vals.sort()

        dummy = ListNode(0)
        tail = dummy
        for val in vals:
            tail.next = ListNode(val)
            tail = tail.next
        return dummy.next   