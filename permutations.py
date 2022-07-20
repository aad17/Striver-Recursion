'''
Print all permutations of the given array
Take a map/freq array which specifies whether the element is taken or not
e.g. nums = [1, 2, 3]
     freq = [False, False, False]
     If taken freq[i] is changed to True
     Ans if len(ds) == len(nums)
     The ds is copied to the ans
     The use of backtracking is done
     While going to another permutation the freq[i] is changed back to False
'''
class Solution:
    def permute(self, nums):
        ans = []
        def recurse(nums, ds, freq):
            if len(ds) == len(nums):
                ans.append(ds.copy())
                return

            for i in range(len(nums)):
                if not freq[i]:
                    freq[i] = True
                    ds.append(nums[i])
                    recurse(nums, ds, freq)
                    ds.pop()
                    freq[i] = False
        
        freq = [False] * len(nums)
        recurse(nums, [], freq)
        return ans

s = Solution()
print(s.permute([1, 2, 3]))