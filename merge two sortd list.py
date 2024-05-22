from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next

# Example usage
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

if __name__ == "__main__":
    # Example usage
    # Creating two linked lists: 1 -> 3 -> 5 -> None and 2 -> 4 -> 6 -> None
    list1 = ListNode(1)
    list1.next = ListNode(3)
    list1.next.next = ListNode(5)

    list2 = ListNode(2)
    list2.next = ListNode(4)
    list2.next.next = ListNode(6)

    print("Original lists:")
    print("List 1:", end=" ")
    print_linked_list(list1)
    print("List 2:", end=" ")
    print_linked_list(list2)

    # Merging the two linked lists
    sol = Solution()
    merged_head = sol.mergeTwoLists(list1, list2)
    print("\nMerged linked list:")
    print_linked_list(merged_head)
