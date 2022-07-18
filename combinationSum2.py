# Brute Force
# Gives TLE

# class Solution:
#     def combinationSum2(self, candidates, target: int):
#         candidates.sort()
#         ans = set()
#         n = len(candidates)
#         def recurse(idx, ds, target, n, ans):
#             if idx == n: 
#                 if target == 0:
#                     ans.add(tuple(ds.copy()))
#                 return
            
#             if candidates[idx] <= target:
#                 ds.append(candidates[idx])
#                 recurse(idx+1, ds, target-candidates[idx], n, ans)
#                 ds.pop()

#             recurse(idx+1, ds, target, n, ans)
            
#         recurse(0, [], target, n, ans)
#         ans = list(map(list, ans))
#         return ans

# s = Solution()
# print(s.combinationSum2([10,1,2,7,6,1,5], 8))

class Solution:
    def combinationSum2(self, candidates, target: int):
        candidates.sort()
        n = len(candidates)
        ans = []
        def recurse(idx, arr, target, ans, ds):
            if target == 0:
                ans.append(ds.copy())
                return

            for i in range(idx, n):
                if i > idx and arr[i] == arr[i-1]:
                    continue
                if arr[i] > target:
                    break

                ds.append(arr[i])
                recurse(i+1, arr, target-arr[i], ans, ds)
                ds.pop()

        recurse(0, candidates, target, ans, [])
        return ans

s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5], 8))
