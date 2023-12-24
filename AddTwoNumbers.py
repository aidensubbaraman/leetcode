# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # Initialise to 0 for first iteration
        remainder = 0

        # STRATEGY: Append to a result list
        dummyNode = ListNode(0)
        tail = dummyNode

        while l1 is not None or l2 is not None or remainder != 0:
            num1 = l1.val if l1 is not None else 0
            num2 = l2.val if l2 is not None else 0

            total = num1 + num2 + remainder
            digit = total % 10
            remainder = total // 10

            # Create the new digit node 
            newleadingNode = ListNode(digit)

            # tail node now points to new node
            tail.next = newleadingNode

            # Make tail node the new node we just made
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        
        resultList = dummyNode.next
        dummyNode.next = None
        return resultList
        