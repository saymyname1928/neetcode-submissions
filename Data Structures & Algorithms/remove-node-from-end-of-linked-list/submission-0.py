# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        cur = head
        while cur: 
            nodes.append(cur)
            cur = cur.next

        if n == 1:
            if len(nodes) == 1:
                return None

            nodes[-2].next = None
            return head

        elif n == len(nodes):
            return nodes[1]

        nodes[-(n+1)].next = nodes[-(n-1)]
        return nodes[0]
        