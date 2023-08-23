class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        curr = head
        while curr.next is not None:
            if curr.val == curr.next.val:
                temp = curr.next
                curr.next = curr.next.next
                del temp
            else:
                curr = curr.next
        return head
