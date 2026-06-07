# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def __init__(self):
        self.head = None
    def insert(self , data):
        newNode = ListNode(data)
        newNode.next = self.head
        self.head = newNode
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr:
            self.insert(curr.val)
            curr = curr.next
        return self.head
        