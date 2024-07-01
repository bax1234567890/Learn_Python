# Reversing a Linked List

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Example usage
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
reversed_head = reverse_linked_list(head)
# Output the reversed linked list
while reversed_head:
    print(reversed_head.value, end=" ")
    reversed_head = reversed_head.next
# Output: 4 3 2 1


# Merging Two Sorted Lists
def merge_sorted_lists(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2
    return dummy.next

# Example usage
l1 = ListNode(1, ListNode(3, ListNode(5)))
l2 = ListNode(2, ListNode(4, ListNode(6)))
merged_head = merge_sorted_lists(l1, l2)
# Output the merged linked list
while merged_head:
    print(merged_head.value, end=" ")
    merged_head = merged_head.next
# Output: 1 2 3 4 5 6