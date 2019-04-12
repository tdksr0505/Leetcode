class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max = 0
        cur_string = ""
        i = 0
        j = 0
        while i < len(s):
            if i+j < len(s) and s[i+j] not in cur_string:
                cur_string += s[i+j]
                if len(cur_string) > max:
                    max = len(cur_string)
                # print cur_string
                j += 1
            else :
                i += 1
                j = 0
                cur_string = ""
        # print max
        return max

sol = Solution()
sol.lengthOfLongestSubstring("pwwkew")
