# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         if len(nums)<3:
#             return []
#         s_nums = sorted(nums)

#         if s_nums[0]>0:
#             return []
        
#         triplets = set()
#         # print(len(s_nums)-1)
#         for l in range(len(s_nums)-2):
#             if s_nums[l]>0:
#                 break
#             # if s_nums[l-1]==s_nums[l]:
#             #     continue
#             p = l+1
#             r = len(s_nums)-1
#             while True:
#                 if r-p<1:
#                     p = l + 1
#                     r = r - 1
#                 if r-l<2:
#                     break
#                 sum = s_nums[l] + s_nums[p] + s_nums[r]
#                 if sum == 0:
#                     triplets.add((s_nums[l] , s_nums[p] , s_nums[r]))
#                     p = l + 1
#                     r = r - 1
#                     continue
#                 if sum <0:
#                     p = p+1
#                     while s_nums[p]==s_nums[p-1] and r-p<1:
#                         p = p+1
#                 if sum >0:
#                     r = r-1
#         return list(triplets)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res