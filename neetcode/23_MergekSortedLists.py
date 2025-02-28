"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []


Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""
from typing import List, Optional



def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    m = len(lists)
    if not lists or m == 0:
        return None
    dummy = ListNode()
    merged = dummy

    def merge(a, b):
        d = ListNode()
        curr = d
        while a and b:
            if a.val < b.val:
                curr.next = a
                curr = a
                a = a.next
            else:
                curr.next = b
                curr = b
                b = b.next
        curr.next = a if a else b
        return d.next

    while len(lists)>1:
        temp = []
        for i in range(0, len(lists),2):
            l1 = lists[i]
            l2 = lists[i+1] if i+1 < len(lists) else None
            temp.append(merge(l1,l2))
        lists = temp

    return lists[0]