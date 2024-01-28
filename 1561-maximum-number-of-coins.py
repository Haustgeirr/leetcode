from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        """
        :type piles: List[int]
        :rtype: int
        """
        self.sum = 0
        if len(piles) <= 0:
            return 0
        
        piles.sort(reverse=True)
        
        for p in range(len(piles) // 3):
            self.sum += piles[p*2+1]
        
        return self.sum


piles = [2,4,1,2,7,8]
print(Solution().maxCoins(piles))