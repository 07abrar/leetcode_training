# Definition for singly-linked list.
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
            cur.next = list1 or list2

        return dummy.next


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

    list1 = list_to_linked_list([1, 2, 4])
    list2 = list_to_linked_list([1, 3, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(linked_list_to_list(result))

    list1 = list_to_linked_list([])
    list2 = list_to_linked_list([])
    result = solution.mergeTwoLists(list1, list2)
    print(linked_list_to_list(result))

    list1 = list_to_linked_list([])
    list2 = list_to_linked_list([0])
    result = solution.mergeTwoLists(list1, list2)
    print(linked_list_to_list(result))
