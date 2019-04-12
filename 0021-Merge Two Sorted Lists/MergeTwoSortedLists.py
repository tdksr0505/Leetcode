#
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if(l1 == None) :
            return l2
        elif(l2 == None):
            return l1
        else :
            l3 = ListNode(None)
            curl = l3
        while l1 is not None or l2 is not None:
            if(l1 is None and l2 is not None):
                nextNode = ListNode(l2.val)
                l2 = l2.next
                curl.next = nextNode
                curl = curl.next
                continue
            if(l2 is None and l1 is not None):
                nextNode = ListNode(l1.val)
                l1 = l1.next
                curl.next = nextNode
                curl = curl.next
                continue
            if(l1.val<l2.val):
                nextNode = ListNode(l1.val)
                l1 = l1.next
                curl.next = nextNode
                curl = curl.next
            else :
                nextNode = ListNode(l2.val)
                l2 = l2.next
                curl.next = nextNode
                curl = curl.next
        return l3.next
