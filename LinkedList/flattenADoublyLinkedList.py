class Solution:
    def flatten(self, head):
        curr = head
        stack = deque()
        while (curr):
            if (curr.child):
                if (curr.next):
                    stack.append(curr.next)
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
            if (not curr.next and stack):
                temp = stack.pop()
                temp.prev = curr
                curr.next = temp
            curr = curr.next
        return head
