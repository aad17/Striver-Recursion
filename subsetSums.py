class Solution():
    def subsetSums(self, arr, N):
        ans = []
        def recurse(idx, arr, ans, ds):
            if idx == N:
                ans.append(sum(ds))
                return
            ds.append(arr[idx])
            recurse(idx+1, arr, ans, ds)
            ds.pop()
            recurse(idx+1, arr, ans, ds)

        recurse(0, arr, ans, [])
        ans.sort()
        return ans

s = Solution()
print(s.subsetSums([5, 2, 1], 3))