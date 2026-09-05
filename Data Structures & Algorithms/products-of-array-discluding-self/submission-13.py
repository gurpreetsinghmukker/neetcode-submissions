from collections import defaultdict
import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_idxs = []
        for i, num in enumerate(nums):
            if num == 0:
                zero_idxs.append(i)
                if len(zero_idxs)>=2:
                    return [0]*len(nums)

        if len(zero_idxs) == 1:
            return_list = [0]*len(nums)
            if len(nums[:zero_idxs[0]]) == 0:
                return_list[zero_idxs[0]] = math.prod(nums[zero_idxs[0]+1:])
            elif len(nums[zero_idxs[0]+1:]) == 0:
                return_list[zero_idxs[0]] = math.prod(nums[:zero_idxs[0]])
            else:
                return_list[zero_idxs[0]] = math.prod(nums[zero_idxs[0]+1:])*math.prod(nums[:zero_idxs[0]])
            return return_list

        elif len(zero_idxs) == 0:
            return_list = []
            prod = math.prod(nums)
            for i, num in enumerate(nums):
                return_list.append(int(prod/num))
            return return_list