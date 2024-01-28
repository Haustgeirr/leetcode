from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #         for n in nums
        #         check if n == n-1
        #         if it does, pop, next n

        last_no = nums[len(nums) - 1]

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] != last_no:
                last_no = nums[i]
            else:
                nums.pop(i)

        return len(nums)


nums = [1, 1, 2, 2, 3]
Solution().removeDuplicates(nums)
# print(len(nums))
print(nums)
