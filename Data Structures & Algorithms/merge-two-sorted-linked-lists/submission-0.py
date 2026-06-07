# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def __init__(self):
        self.head = None
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def traverse(list1,temp):
            curr = list1
            while curr:
                temp.append(curr.val)
                curr = curr.next
        def insertend(data):
            newNode = ListNode(data)
            if self.head is None:
                self.head = newNode
                return 
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode  

        temp = []
        traverse(list1 , temp)
        traverse(list2 , temp)
        temp.sort()
        for i in temp:
            insertend(i)
        return self.head
        