from collections import defaultdict
import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        digit_counter = defaultdict(int)
        zero_idxs = [] if not nums[0]==0 else [0]
        digit_counter[0] = 0 if not nums[0]==0 else 1
        prod = nums[0] if not nums[0]==0 else 1
        for i, num in enumerate(nums[1:], start = 1):
            digit_counter[num]+=1
            if num == 0:
                zero_idxs.append(i)
            else:
                prod = prod * num
            if digit_counter[0] >= 2:
                return [0]*len(nums)
        if digit_counter[0] == 1:
            return_list = [0]*len(nums)
            return_list[zero_idxs[0]] = prod
            return return_list

        elif digit_counter[0] == 0:
            return_list = []
            for i, num in enumerate(nums):
                return_list.append(int(prod/num))
            return return_list