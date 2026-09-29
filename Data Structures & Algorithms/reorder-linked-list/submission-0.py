# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        root = head
        heads = [head]
        while head.next is not None:
            heads.append(head.next)
            head = head.next

        head = heads.pop(0)
        # print(head.val)
        # print([e.val for e in heads])
        for i in range(len(heads)):
            if i % 2 == 0:
                head.next = heads.pop()
            else:
                head.next = heads.pop(0)
            head = head.next
            print(head.val)
        head.next = None
            
