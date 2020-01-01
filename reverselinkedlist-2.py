# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        li = ListNode(-1)
        li.next = head
        prev = li
        curr = prev.next
        counter = 1
        
        while counter < m:
            prev = prev.next
            counter += 1
        print(counter)
        
        curr = prev.next
        reversed_head = None
        
        while counter >=m and counter <=n:
            temp = curr.next
            curr.next = reversed_head
            reversed_head = curr
            curr = temp
            counter +=1
        prev.next.next = curr
        prev.next = reversed_head
        return li.next
    
    
