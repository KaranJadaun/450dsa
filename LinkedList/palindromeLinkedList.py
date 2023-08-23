class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def middle(head):
            slow, fast = head, head.next
            while (fast and fast.next): slow, fast = slow.next, fast.next.next
            return slow
        def reverse(head):
            prev, curr = None, head
            while (curr):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        if (head.next is None): return True
        mid = middle(head)
        temp = mid.next
        mid.next = reverse(temp)
        temp1, temp2 = head, mid.next
        while (temp2):
            if (temp1.val != temp2.val): return False
            else: temp1, temp2 = temp1.next, temp2.next
        return True
