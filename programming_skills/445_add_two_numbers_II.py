# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number1 = int(''.join(map(str, linked_list_to_list(l1))))
        number2 = int(''.join(map(str, linked_list_to_list(l2))))
        summation = number1 + number2
        sum_list = list(map(int, str(summation)))
        return list_to_linked_list(sum_list)


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

    list1 = list_to_linked_list([7, 2, 4, 3])
    list2 = list_to_linked_list([5, 6, 4])
    result = solution.addTwoNumbers(list1, list2)
    print(linked_list_to_list(result))

    list1 = list_to_linked_list([2, 4, 3])
    list2 = list_to_linked_list([5, 6, 4])
    result = solution.addTwoNumbers(list1, list2)
    print(linked_list_to_list(result))

    list1 = list_to_linked_list([0])
    list2 = list_to_linked_list([0])
    result = solution.addTwoNumbers(list1, list2)
    print(linked_list_to_list(result))
