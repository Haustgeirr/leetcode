class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = ''.join(filter(str.isalnum, s)).lower()
        i = 0
        print(p)
        print(len(p))
        print(len(p) // 2)
        while i < len(p) // 2:
            print(str(i) + ' ' + p[i] + ' == ' + p[-1-i])
            if(p[i] != p[-1-i]):
                return False
            i += 1
        return True


s = "0P"

print(Solution().isPalindrome(s))
