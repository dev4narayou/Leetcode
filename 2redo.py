from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)  # Dummy node to simplify code
        curr_node = dummy_head
        carry = 0  # Carry over value
        
        while l1 is not None or l2 is not None or carry != 0:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            sum_res = val1 + val2 + carry
            
            carry = sum_res // 10
            new_digit = sum_res % 10
            
            curr_node.next = ListNode(new_digit)
            curr_node = curr_node.next
            
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        return dummy_head.next

# Helper function to create a linked list from a list
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to print linked list
def print_linked_list(node):
    while node is not None:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

if __name__ == "__main__":
    # Example usage:
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    
    print("Result:")
    print_linked_list(result)
