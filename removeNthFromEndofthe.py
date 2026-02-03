class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 1
        temp = head
        while temp:
            temp = temp.next
            count += 1
        
        
        temp2 = head

        newNode = ListNode()
        resNode = newNode
        
        count2 = 0
        while temp2:
            count2 += 1
            if (count - count2) != n:
                tempNode = ListNode(temp2.val)
                newNode.next = tempNode
                newNode = tempNode

            temp2 = temp2.next
        return resNode.next

