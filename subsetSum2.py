class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        n = len(nums)
        ans = []
        def recurse(idx, nums, ds, ans):
            ans.append(ds.copy())
            for i in range(idx, n):
                if i != idx and nums[i] == nums[i-1]:
                    continue
                ds.append(nums[i])
                recurse(idx+1, nums, ds, ans)
                ds.pop()

        recurse(0, nums, [], ans)
        return ans

s = Solution()
print(s.subsetsWithDup([1, 2, 3]))