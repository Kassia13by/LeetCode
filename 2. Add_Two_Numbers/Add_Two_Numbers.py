# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        newl1 = []
        current = l1
        
        # Traverse the linked list
        while current:
            newl1.append(current.val)  
            current = current.next

        newl2 = []
        current = l2

        while current:
            newl2.append(current.val)
            current = current.next
        
        l1_number = 0
        for i in range(len(newl1)):
            l1_number = l1_number * 10 + newl1[-(i+1)]

        l2_number = 0
        for i in range(len(newl2)):
            l2_number = l2_number * 10 + newl2[-(i+1)]
        
        sumup = str(l1_number + l2_number)
        sumup_ls = []
        for i in range(len(sumup)):
            sumup_ls.append(int(sumup[-(i+1)]))


        head = ListNode(sumup_ls[0])
        current = head
    
        for value in sumup_ls[1:]:
            current.next = ListNode(value)
            current = current.next
    
        return head