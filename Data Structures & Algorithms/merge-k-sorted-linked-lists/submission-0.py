# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: 
    def __init__(self):
        self.head = None  
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def listing(head , lst):
            curr = head
            while curr:
                lst.append(curr.val)
                curr = curr.next
        def insert(data):
            newNode = ListNode(data)
            if self.head is None:
                self.head = newNode
                return
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode 

        lis = []
        curr = lists
        for temp in lists:
            listing(temp , lis)
        lis.sort()
        for i in lis:
            insert(i)
        return self.head
