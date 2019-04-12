class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        list = []
        num = abs(x)
        while num > 0:
            list.append(num%10)
            num /= 10

        list.reverse()

        n = 1
        result = 0
        for i, elem in enumerate(list):
            result += n*elem
            n *= 10

        if result > 2**31-1 :
            return 0
        if x < 0:
            return 0-result
        else:
            return result
sol = Solution()
sol.reverse(-230)

x = 123456789
print str(x)[1:8:2]
