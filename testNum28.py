# 作者 ljc
str = 'aaad'
print(str[3:5])


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == needle:
            return len(haystack)
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


solution = Solution()
print(solution.strStr('b', 'b'))
