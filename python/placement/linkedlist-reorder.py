class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reorder_linked_list(head):
    if not head or not head.next:
        return head

    # Find the middle of the linked list
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Split the linked list into two halves
    second_half = slow.next
    slow.next = None

    # Reverse the second half of the linked list
    prev = None
    current = second_half
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    second_half = prev

    # Merge the two halves alternately
    first_half = head
    while second_half:
        next_node1 = first_half.next
        next_node2 = second_half.next
        first_half.next = second_half
        second_half.next = next_node1
        first_half = next_node1
        second_half = next_node2

    return head

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Example usage:
if __name__ == "__main__":
    # Create a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print("Original Linked List:")
    print_linked_list(head)

    head = reorder_linked_list(head)

    print("Reordered Linked List:")
    print_linked_list(head)