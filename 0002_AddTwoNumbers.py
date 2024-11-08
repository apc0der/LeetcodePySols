class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        Q = ListNode() # build a new list
        temp = Q # traversal node
        carry = 0 # carry value
        while True: # loop continuously
            s = carry # sum starts out with carry
            if l1 is not None: # if digits left to process
                s += l1.val
                l1 = l1.next
            if l2 is not None: # same for number 2
                s += l2.val
                l2 = l2.next
            carry = s // 10 # next carry 
            temp.val = int(s % 10) # load the digit into the node
            if l1 is not None or l2 is not None or carry != 0: # if another node is required
                # allocate a new node and move on
                n = ListNode()
                temp.next = n
                temp = temp.next
            else: # otherwise we are done
                break
        return Q
