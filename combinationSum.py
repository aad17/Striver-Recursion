class Solution:
    def combinationSum(self, candidates, target: int):
        n = len(candidates)
        ans = []
        def helper(candidates, target, ds, idx, n):
            if idx >= n:
                if target == 0:
                    ans.append(ds.copy())
                return
            
            if candidates[idx] <= target:
                ds.append(candidates[idx])
                helper(candidates, target - candidates[idx], ds, idx, n)
                ds.pop()
            
            helper(candidates, target, ds, idx+1, n)
        
        helper(candidates, target, [], 0, n)
        return ans

s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))