# Brute Force
# class Solution:
#     def getPermutation(self, n: int, k: int) -> str:
#         ans = []
#         op = ''
#         used = [False for _ in range(n)]
#         myset = [str(i+1) for i in range(n)]
#         if n == 1:
#             return '1'
#         def recurse(idx, ds, n):
#             nonlocal op
#             if len(ds) == n:
#                 ans.append(ds.copy())
#                 return
#             for i in range(n):
#                 if len(ans) >= k:
#                     op = ''.join(ans[k-1])
#                     return
#                 if not used[i]:
#                     used[i] = True
#                     ds.append(myset[i])
#                     recurse(i+1, ds, n)
#                     ds.pop()
#                     used[i] = False

#         recurse(0, [], n)
#         return op
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = 1
        numbers = []
        for i in range(1, n):
            fact *= i
            numbers.append(i)

        numbers.append(n)
        ans = ''
        k = k - 1
        while True:
            ans = ans + str(numbers[int(k/fact)])
            numbers.pop(int(k/fact))
            if len(numbers) == 0:
                break
            k = k % fact
            fact = int(fact / len(numbers))

        return ans

s = Solution()
print(s.getPermutation(4, 9))