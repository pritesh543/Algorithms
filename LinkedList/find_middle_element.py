# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        ############ Approach -1 ###########
        
        # Count the number of nodes in the list
        # Find middle element & return
        
        """
        
        total_nodes = 0
        x = head
        while x:
            total_nodes += 1
            x = x.next
        
        ## Trick-1 ##
        middle_element = total_nodes//2
        count = 0
        while head:
            if count == middle_element:
                return head
            head = head.next
            count += 1
            
        ## Trick-2 ##
        x = head
        for _ in range(total_nodes>>1):
            x = x.next
        
        return x

        """
        
        ########## Approach -2 ############
        
        # Move Pointers (starts with head)
        # 1st pointer - 1 increment
        # 2nd Pointer - 2 increments
        
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
                
        return slow
        """
        
        ############ Approach -3 #############
        if(head.next==None):
            return head
        
        headPointer = head
        length = 0
        i = 0
        while(True):
            head = head.next
            length += 1
            
            if(i!= length // 2):
                while(i!=length//2):
                    i += 1
                    headPointer = headPointer.next
            
            #print("i: ", i)
            #print("headPointer: ", headPointer)
            #print("while-length: ", length)
            #print("\n")
            
            if(head.next==None):
                length += 1
                if(i!=length // 2):
                    while(i!=length//2):
                        i += 1
                        headPointer = headPointer.next
                
                #print("==============================")
                #print("headPointer:[if] ", headPointer)
                #print("==============================")
                
                return headPointer

        ############### Approach - 4 ###############
        
        d = {}
        p = 0
        while head:
            d[p] = head
            head = head.next
            p += 1
            
        return d[p//2]
    
        