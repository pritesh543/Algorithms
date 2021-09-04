# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        ###### Recursion Approach ########
        """
        def binary_to_decimal(cur, value):
            if not cur:
                return value
            
            else:
                return binary_to_decimal(cur.next, value=(value<<1)+cur.val)
            
        # Recursion Ends #
        
        return binary_to_decimal(cur=head, value=0)
        """
        
        ###### int() function Approach #########
        """
        binary = ""
        x = head
        while x:
            binary += str(x.val)
            x = x.next
        
        return int(binary, 2)
        """
        
        ######## left shift Approach (Un-comprehensive) ########
        binary = 0
        while head:
            binary = (binary<<1) + head.val
            head = head.next
        
        return binary
