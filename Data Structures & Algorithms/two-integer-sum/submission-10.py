
import math
class Solution:


    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])

        A.sort()

        def find(num_list , num):
            length = len(num_list)
            mid = length // 2
            if length % 2 != 0:
                mid_point = mid
            else:
                mid_point = mid - 1

            if len(num_list)==0:
                return None
            
            elif len(num_list)==1:
                if num_list[0][0] == num:
                    return 0
                else:
                    return None
            elif num < num_list[mid_point][0]:
                idx = find(num_list[:mid_point], num)
                return idx if not idx==None else None
            elif num == num_list[mid_point][0]:
                return mid_point
            else:
                idx = find(num_list[mid_point+1:], num)
                return mid_point + idx + 1 if not idx==None else None

        for i, val1 in enumerate(A):
            other_num = target - val1[0]
            if other_num == val1[0]:
                return [val1[1], A[i+1][1]]
            idx = find(A, other_num)
            if idx:
                return [min(val1[1], A[idx][1]), max(val1[1], A[idx][1])]

            

        # for i, val1 in enumerate(nums):
        #     for j, val2 in enumerate(nums):
        #         if val1+val2 == target and not i == j:
        #             return [min(i,j), max(i,j)]



