class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in range(0,len(t)):
            if s[i] == t[i]:
                pass


sol = Solution()
s = "abc"
t = "ahbgdc"
print(sol.isSubsequence(s,t))