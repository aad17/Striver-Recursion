class Solution:
    def partition(self, s: str):
        self.ans = []
        ds = []
        self.recurse(0, ds, s)
        return self.ans

    def recurse(self, idx, ds, s):
        if idx == len(s):
            self.ans.append(ds[:])
            return
        
        for i in range(idx, len(s)):
            if s[idx:i+1] == s[idx:i+1][::-1]:
                ds.append(s[idx:i+1])
                self.recurse(i+1, ds, s)
                ds.pop()

        return


s = Solution()
print(s.partition("aab"))