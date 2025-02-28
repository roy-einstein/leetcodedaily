"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.



Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]


Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""

from collections import deque
from typing import Optional
"""
Logic:
Approach and Theory
The solution can be broken down into three key steps:

Step 1: Splitting the List into Two Halves
Using the two-pointer technique, we can identify the middle of the list:

slow moves one step at a time.
fast moves two steps at a time.
When fast reaches the end, slow will be at the midpoint of the list.

Example:

Input: 1 → 2 → 3 → 4 → 5
After splitting: 1 → 2 → 3 and 4 → 5
Step 2: Reversing the Second Half
Next, we reverse the second half of the list. Starting from the node after slow, we use a standard iterative reversal process to reverse the pointers.

Example:

Before reversing: 4 → 5
After reversing: 5 → 4
Step 3: Merging the Two Halves
Finally, we merge the two halves alternately:

Take a node from the first half, then a node from the reversed second half.
Repeat until all nodes are merged.
Example:

First half: 1 → 2 → 3
Reversed second half: 5 → 4
Merged: 1 → 5 → 2 → 4 → 3
"""

def reorderList(head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    fast = head
    slow = head

    while fast or fast.next:
        fast = fast.next.next
        slow = slow.next

    l1 = slow.next
    slow.next = None
    prev = None
    while l1:
        temp = l1.next
        l1.next = prev
        prev = l1
        l1 = temp

    first = head
    second = prev

    while second:
        temp1 = first.next
        temp2 = second.next

        first.next = second
        second.next = temp1

        first = temp1
        second = temp2




