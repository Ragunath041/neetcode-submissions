# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        lis = []
        curr = head
        while curr:
            lis.append(curr.val)
            curr = curr.next
        i = 0
        j = len(lis) - 1
        curr = head
        turn = True
        while i <= j and curr:
            if turn:
                curr.val = lis[i]
                i += 1
            else:
                curr.val = lis[j]
                j -= 1
            curr = curr.next
            turn = not turn
