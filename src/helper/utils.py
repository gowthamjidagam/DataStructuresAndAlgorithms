class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def list_to_linked_list(lst):
    """
    Convert Python list to linked list
    Returns head node of the linked list
    """
    if not lst:
        return None

    head = Node(lst[0])
    current = head

    for item in lst[1:]:
        current.next = Node(item)
        current = current.next

    return head


# Helper function to display linked list
def print_linked_list(head):
    """Print linked list given head node"""
    current = head
    while current:
        print(current.val, end=" -> " if current.next else " -> None\n")
        current = current.next

if __name__ == "__main__":
    # Example usage
    my_list = [1, 2, 3, 4, 5]
    head = list_to_linked_list(my_list)
    print_linked_list(head)
    # Output: 1 -> 2 -> 3 -> 4 -> 5 -> None
