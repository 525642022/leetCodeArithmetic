# 作者 ljc

# 我们正在玩一个猜数字游戏。 游戏规则如下：
# 我从 1 到 n 选择一个数字。 你需要猜我选择了哪个数字。
# 每次你猜错了，我会告诉你这个数字是大了还是小了。
# 你调用一个预先定义好的接口 guess(int num)，它会返回 3 个可能的结果（-1，1 或 0）：
#
# -1 : 我的数字比较小
#  1 : 我的数字比较大
#  0 : 恭喜！你猜对了！
# 示例:
#
# n = 10, 我选择 6.
#
# 返回 6.
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        while low <= high:
            mid = (high +low)/2
            ans = guess(mid)
            if ans == 0:
                return mid
            elif ans == -1:
                high = mid -1
            else :
                low = mid +1