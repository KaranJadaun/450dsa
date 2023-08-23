class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        temp = dummy
        carry = 0
        while (l1 or l2 or carry == 1):
            s = 0
            if (l1):
                s += l1.val
                l1 = l1.next
            if (l2):
                s += l2.val
                l2 = l2.next
            s += carry
            carry = s // 10
            Node = ListNode(s % 10)
            temp.next = Node
            temp = temp.next
        return dummy.next
