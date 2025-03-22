# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # creating list of current nodes
        valid_lists = []
        for linked_list_node in lists:
            if linked_list_node is not None:
                valid_lists.append(linked_list_node)

        # init a linked list to return
        dummy_return_node = ListNode()
        current_node = dummy_return_node
        
        # merging
        while len(valid_lists) > 0:
            smallest_value = valid_lists[0].val
            smallest_node = valid_lists[0]
            smallest_index = 0
            for i in range(1, len(valid_lists)):
                if valid_lists[i].val < smallest_value:
                    smallest_value = valid_lists[i].val
                    smallest_node = valid_lists[i]
                    smallest_index = i
            # adds smallest node to linked list to return
            current_node.next = smallest_node
            current_node = current_node.next
            # remove node from valid_lists because it has been accounted for
            if smallest_node.next is None:
                del valid_lists[smallest_index]
            else:
                valid_lists[smallest_index] = smallest_node.next
        
        # return start of valid linked-list
        return dummy_return_node.next

                    


        