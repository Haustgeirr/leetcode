class Solution:
    def countConsistentStrings(self, allowed, words):
        self.sum = 0
        for w in words:
            isConsistent = True
            for l in w:
                if l not in allowed:
                    isConsistent = False
            
            if isConsistent:
                self.sum += 1
        
        return self.sum

allowed1 = "ab"
words1 = ["ad","bd","aaab","baa","badab"]

allowed2 = "abc"
words2 = ["a","b","c","ab","ac","bc","abc"]

allowed3 = "cad"
words3 = ["cc","acd","b","ba","bac","bad","ac","d"]

res1 = Solution().countConsistentStrings(allowed1, words1)
res2 = Solution().countConsistentStrings(allowed2, words2)
res3 = Solution().countConsistentStrings(allowed3, words3)

print(res1)
print(res2)
print(res3)