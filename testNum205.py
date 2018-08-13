# 作者 ljc
# 给定两个字符串 s 和 t，判断它们是否是同构的。
#
# 如果 s 中的字符可以被替换最终变成 t ，则两个字符串是同构的。
#
# 所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。
#
# 例如，
#
# 给定 "egg", "add", 返回 true.
#
# 给定 "foo", "bar", 返回 false.
#
# 给定 "paper", "title", 返回 true.
#
# 注意：
#
# 你可以假设 s 和 t 具有相同的长度。

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1, d2 = {}, {}
        for i, val in enumerate(s):
            d1[val] = d1.get(val, []) + [i]
        for i, val in enumerate(t):
            d2[val] = d2.get(val, []) + [i]
        return sorted(d1.values()) == sorted(d2.values())

    def isIsomorphic2(self, s, t):
        d1, d2 = [[] for _ in range(256)], [[] for _ in range(256)]
        for i, val in enumerate(s):
            d1[ord(val)].append(i)
        for i, val in enumerate(t):
            d2[ord(val)].append(i)
        return sorted(d1) == sorted(d2)

    def isIsomorphic3(self, s, t):

        return len(set(zip(s, t))) == len(set(s)) == len(set(t))

    def isIsomorphic4(self, s, t):
        return [s.find(i) for i in s] == [t.find(j) for j in t]

    def isIsomorphic5(self, s, t):
        return map(s.find, s) == map(t.find, t)

    def isIsomorphic(self, s, t):
        d1, d2 = [0 for _ in range(256)], [0 for _ in range(256)]
        for i in range(len(s)):
            if d1[ord(s[i])] != d2[ord(t[i])]:
                return False
            d1[ord(s[i])] = i + 1
            d2[ord(t[i])] = i + 1
        return True
solution = Solution()
solution.isIsomorphic3('abcad','bcdba')