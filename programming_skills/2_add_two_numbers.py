# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number1 = self.reversed_linked_list_to_number(l1)
        number2 = self.reversed_linked_list_to_number(l2)
        summation = number1 + number2
        sum_list = list(map(int, str(summation)))
        sum_list.reverse()
        return list_to_linked_list(sum_list)

    def reversed_linked_list_to_number(self, head):
        current = None
        node = head
        while node:
            next_node = node.next
            node.next = current
            current, node = node, next_node
        new_list = linked_list_to_list(current)
        return int(''.join(map(str, new_list)))


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

    list1 = list_to_linked_list([2, 4, 3])
    list2 = list_to_linked_list([5, 6, 4])
    result = solution.addTwoNumbers(list1, list2)
    print(linked_list_to_list(result))

    list1 = list_to_linked_list([0])
    list2 = list_to_linked_list([0])
    result = solution.addTwoNumbers(list1, list2)
    print(linked_list_to_list(result))

    list1 = list_to_linked_list([9, 9, 9, 9, 9, 9, 9])
    list2 = list_to_linked_list([9, 9, 9, 9])
    result = solution.addTwoNumbers(list1, list2)
    print(linked_list_to_list(result))
