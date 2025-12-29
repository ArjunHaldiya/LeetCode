# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy head for the result list and a pointer to the current node
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Loop while there are still digits in either list or a carry is present
        while l1 or l2 or carry:
            # Get the values from the current nodes, defaulting to 0 if the list is exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum of the digits and the current carry
            total_sum = val1 + val2 + carry
            
            # Update carry for the next iteration
            carry = total_sum // 10
            
            # Create a new node with the current digit (sum % 10)
            current.next = ListNode(total_sum % 10)
            
            # Move the current pointer forward
            current = current.next
            
            # Move the input list pointers forward if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        # The result linked list starts from the next of the dummy head
        return dummy_head.next

