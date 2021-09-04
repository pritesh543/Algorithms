# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        ####### Approach -1 ########
        
        # using temp variable
        # for intermediate store
        
        """
        temp = node.next
        node.val = temp.val
        node.next = temp.next
        del temp
        """
        
        ## Trick-2 | Without Temp ##
        
        n = node
        if n == None:
            return
        
        n.val = node.next.val
        n.next = n.next.next

        ## Trick-3 | One Liner ##
        
        node.next, node.val = node.next.next, node.next.val