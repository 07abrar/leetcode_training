# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = None
        node = head
        while node:
            next_node = node.next
            node.next = current
            current, node = node, next_node
        return current


# Helper functions
def list_to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


if __name__ == "__main__":
    solution = Solution()

    head = list_to_linked_list([1, 2, 3, 4, 5])
    result = solution.reverseList(head)
    print(linked_list_to_list(result))

    head = list_to_linked_list([1, 2])
    result = solution.reverseList(head)
    print(linked_list_to_list(result))

    head = list_to_linked_list([])
    result = solution.reverseList(head)
    print(linked_list_to_list(result))
