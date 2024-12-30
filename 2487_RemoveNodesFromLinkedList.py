class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head: # valid node
            head.next = self.removeNodes(head.next) # populate the next node
            if head.next and head.val < head.next.val: # if not none, and we need to cut current element
                return head.next # return the next element
            return head # otherwise, include the head
        return None # otherwise return none
