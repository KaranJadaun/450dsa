class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if (not head): return head
        curr = head
        hashmap = {}
        while (curr):
            copy = Node(curr.val)
            hashmap[curr] = copy
            curr = curr.next
        curr = head
        while (curr):
            copy = hashmap[curr]
            if (curr.next is not None):
                copy.next = hashmap[curr.next]
            if (curr.random is not None):
                copy.random = hashmap[curr.random]
            curr = curr.next
        return hashmap[head]
