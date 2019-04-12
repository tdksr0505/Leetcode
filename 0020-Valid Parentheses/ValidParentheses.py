class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for i, elem in enumerate(s):
            # print stack, elem
            if(elem=="(" or elem=="[" or elem=="{"):
                 stack.append(elem)
            else :
                if len(stack)==0:
                    return False
                if(elem==")"):
                    if(stack[len(stack)-1]!="("):
                        return False
                elif(elem=="]"):
                    if(stack[len(stack)-1]!="["):
                        return False
                elif(elem=="}"):
                    if(stack[len(stack)-1]!="{"):
                        return False


                stack.pop()

        if(len(stack)==0):
            return True
        return False
sol = Solution()
print sol.isValid("]")
