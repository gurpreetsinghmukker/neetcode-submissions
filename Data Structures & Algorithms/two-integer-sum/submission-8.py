
import math
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     def find(num_list , num):
    #         mid_point = math.floor((len(num_list)-1)//2) 
    #         if len(num_list)==1:
    #             if num_list[0] == num:
    #                 return 0
    #             else:
    #                 return None
    #         elif num < num_list[mid_point]:
    #             idx = find(num_list[:mid_point], num)
    #             return idx if not idx==None else None
    #         elif num == num_list[mid_point]:
    #             return mid_point
    #         else:
    #             idx = find(num_list[mid_point+1:], num)
    #             return mid_point + idx + 1 if not idx==None else None

    #     for i, val1 in enumerate(nums):
    #         other_num = target - val1
    #         if other_num == val1:
    #             return [i, i+1]
    #         idx = find(nums, other_num)
    #         # print(idx)
    #         if idx:
    #             return [min(i, idx), max(i,idx)]

            

        for i, val1 in enumerate(nums):
            for j, val2 in enumerate(nums):
                if val1+val2 == target and not i == j:
                    return [min(i,j), max(i,j)]



