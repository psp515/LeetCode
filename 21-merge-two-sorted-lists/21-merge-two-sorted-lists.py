# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        main = ListNode()
        head = main

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                next = list1.next
                main.next = list1
                list1 = next
            else:
                next = list2.next
                main.next = list2
                list2 = next
            main = main.next

        if list1 == None:
            main.next = list2
        else:
            main.next = list1

        return head.next