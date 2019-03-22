# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        list_length = 0
        
        # Count number of nodes (and get list length)
        curr_node = head
        while curr_node is not None:
            list_length += 1
            curr_node = curr_node.next
        
        curr_node = head
        prev_node = None
        right_node = None
        
        left_pointer = None
        right_pointer = None
        
        # How many nodes to check for palindrome?
        move_count = int(list_length / 2)
        
        # Move pointers while reversing list until reaching the "center"
        for _ in range(move_count):
            right_node = curr_node.next
            curr_node.next = prev_node

            prev_node = curr_node
            curr_node = right_node
            
        # Get left and right pointers
        left_pointer = prev_node
        right_pointer = curr_node if list_length % 2 == 0 else curr_node.next
        
        for _ in range(move_count):
            if left_pointer.val != right_pointer.val:
                return False
            
            left_pointer = left_pointer.next
            right_pointer = right_pointer.next
        
        return True
