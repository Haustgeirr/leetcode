class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        length = len(nums)
        result = 0

        while i < length - 1:
            j = i + 1
            while j < length:
                if nums[i] == nums[j]:
                    result += 1
                j += 1
            i += 1

        return result


input1 = [1, 2, 3, 1, 1, 3]
input2 = [1, 1, 1, 1]
input3 = [1, 2, 3]

results = []
results.append(Solution().numIdenticalPairs(input1))
results.append(Solution().numIdenticalPairs(input2))
results.append(Solution().numIdenticalPairs(input3))

print(results)
