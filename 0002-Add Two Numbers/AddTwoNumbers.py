class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def printNode(self) :
        while self != None:
            print self.val
            self = self.next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        num2 = 0
        n = 1


        while l1 != None:
            num1 += l1.val*n
            l1 = l1.next
            n *= 10
        n = 1
        while l2 != None:
            num1 += l2.val*n
            l2 = l2.next
            n *= 10
        total = num1 + num2
        # print total

        l3 = ListNode(total%10)
        total /= 10
        curNode = l3
        while total > 0 :
            newNode = ListNode(total%10)
            curNode.next = newNode
            curNode = curNode.next
            total /= 10
        return l3

node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)
node1.next = node2
node2.next = node3


node4 = ListNode(5)
node5 = ListNode(6)
node6 = ListNode(4)
node4.next = node5
node5.next = node6

# s = node1
# s = s.next
#
# print s.val
sol = Solution()
x = sol.addTwoNumbers(node1, node4)
