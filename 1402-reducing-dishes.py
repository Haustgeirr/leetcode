class Solution(object):

    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        result = 0
        total = 0
        satisfaction.sort()

        while satisfaction and satisfaction[-1] + total > 0:
            total += satisfaction.pop()
            result += total
        return result

    # My garabage code below:

    #     total = float('-inf')
    #     satisfaction.sort(reverse=True)

    #     while len(satisfaction) > 1:
    #         out = self.helper(satisfaction)
    #         if out >= total:
    #             total = out
    #             satisfaction.pop(-1)
    #         else:
    #             return total

    #     if satisfaction[0] <= 0:
    #         return 0

    #     return satisfaction[0]

    # def helper(self, satisfaction):
    #     total = 0
    #     i = 1
    #     while i <= len(satisfaction):
    #         total += i * satisfaction[-i]
    #         i += 1
    #     return total


input1 = [-1, -8, 0, 5, -9]
# output = 14
input2 = [4, 3, 2]
# output = 20
input3 = [-1, -4, -5]
# output = 0
input4 = [-2, 5, -1, 0, 3, -3]
# output = 35
input5 = [2, -2, -3, 1]
# output = 6

results = []
results.append(Solution().maxSatisfaction(input1))
results.append(Solution().maxSatisfaction(input2))
results.append(Solution().maxSatisfaction(input3))
results.append(Solution().maxSatisfaction(input4))
results.append(Solution().maxSatisfaction(input5))

# print([14, 20, 0, 35, 6])
print(results)
