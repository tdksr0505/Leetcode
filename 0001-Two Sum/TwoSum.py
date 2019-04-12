class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}

        for i, elem in enumerate(nums):
            if dict.has_key(elem) :
                return [dict[elem], i]
            else:
                dict[target-elem] = i
sol = Solution()
print sol.twoSum([3,2,4], 6)
