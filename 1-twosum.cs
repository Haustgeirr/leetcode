using System;
using System.Collections;

namespace leetcode
{
    public class TwoSum
    {
        public static int[] nums = new int[] { 2, 7, 11, 15 };
        public static int target = 9;

        public static void Test()
        {
            int[] result = Solution(nums, target);
            Console.WriteLine(result);
        }

        static int[] Solution(int[] nums, int target)
        {
            // Given nums = [2, 7, 11, 15], target = 9,

            // Because nums[0] + nums[1] = 2 + 7 = 9,
            // return [0, 1].

            // Brute Force
            // for (int i = 0; i < nums.Length; i++)
            // {
            //     for (int j = 0; j < nums.Length; j++)
            //     {
            //         if (i == j)
            //             continue;

            //         if (nums[i] + nums[j] == target)
            //         {
            //             return new int[] { i, j };
            //         }
            //     }
            // }

            // Hashtable Two-Pass
            // Hashtable numsHash = new Hashtable();
            // int key = 1;

            // for (int i = 0; i < nums.Length; i++)
            // {
            //     numsHash.Add(i, nums[i]);
            // }

            // for (int i = 0; i < nums.Length; i++)
            // {
            //     int complement = target - nums[i];

            //     if (numsHash.ContainsKey(complement) && (int)numsHash[complement] != i)
            //     {
            //         return new int[] { i, (int)numsHash[complement] };
            //     }
            // }

            // Hashtable One-Pass
            Hashtable numsHash = new Hashtable();

            for (int i = 0; i < nums.Length; i++)
            {
                int complement = target - nums[i];
                if (numsHash.ContainsKey(complement))
                {
                    return new int[] { i, (int)numsHash[complement] };
                }
                numsHash.Add(nums[i], i);
            }
            throw new Exception("No Two Sum solution");
        }
    }
}