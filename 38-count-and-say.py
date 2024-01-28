class Solution:
    def countAndSay(self, n: int) -> str:
        if(n == 1):
            return "1"
        input = "1"
        i = 1
        while i <= n:
            j = 1
            prev = input[0]
            freq = 1
            out = ""
            while j < len(input):
                if(input[j] == prev):
                    freq += 1
                else:
                    out += str(freq) + prev
                    prev = input[j]
                    freq = 1
                j += 1
            out += str(freq) + prev
            input = out
            i += 1
        return input


n = 30
Solution().countAndSay(n)
