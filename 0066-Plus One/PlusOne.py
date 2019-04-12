class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits)-1
        while 1:
            if(digits[i] != 9):
                digits[i] = digits[i] + 1
                return digits
            else:
                digits[i] = 0
                if (i == 0):
                    digits.insert(0, 1)
                    return digits
                i = i - 1



digits = [9,9,9]
sol = Solution()
output = sol.plusOne(digits)
print(output)
