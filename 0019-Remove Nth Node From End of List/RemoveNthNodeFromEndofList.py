
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def listLen(self, head):
        i = 0
        while head != None:
            i += 1
            if(head.next!=None):
                head = head.next
            else :
                return i
        return i

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        i = 0
        len = self.listLen(head)
        cur = head

        while 1:
            if i == len-n :
                if i == 0 :
                    return head.next
                pre.next = cur.next
                cur.next = None
                return head

            pre = cur
            cur = cur.next
            i += 1
