"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        nodes = []
        new_nodes = []
        n2n = dict()

        cur = head
        while cur:
            nodes.append(cur)
            new_node = Node(cur.val, None, cur.random)
            new_nodes.append(new_node)
            n2n[cur] = new_node
            cur = cur.next

        if not nodes:
            return None
        
        for i in range(len(new_nodes)):
            if i < len(new_nodes) - 1:
                new_nodes[i].next = new_nodes[i+1]
            if new_nodes[i].random is not None:
                new_nodes[i].random = n2n[new_nodes[i].random]
        
        return new_nodes[0]
            

        
            