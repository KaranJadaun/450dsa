class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hash = set()
        if head is None or head.next is None:
            return head
        curr = head
        hash.add(curr.val)
        while curr.next:
            if curr.next.val in hash:
                curr.next = curr.next.next
            else:
                hash.add(curr.next.val)
                curr = curr.next
        return head
