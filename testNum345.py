# 作者 ljc
# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
#
# 示例 1：
# 给定 s = "hello", 返回 "holle".
#
# 示例 2：
# 给定 s = "leetcode", 返回 "leotcede".
#
# 注意:
# 元音字母不包括 "y".
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        L = list(s)
        i = 0
        j = len(L) - 1
        while i < j:
            while i < j and L[i] not in vowels:
                i += 1
            while i < j and L[j] not in vowels:
                j -=1
            L[i], L[j] = L[j], L[i]
            i += 1
            j -= 1
        return ''.join(L)