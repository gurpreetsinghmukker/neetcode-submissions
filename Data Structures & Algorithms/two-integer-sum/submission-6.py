class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, val1 in enumerate(nums):
            for j, val2 in enumerate(nums):
                if val1+val2 == target and not i == j:
                    return [min(i,j), max(i,j)]
        # nums_set = set(nums)
        # comb_set = set()
        # for i in range(target+1):
        #     m = min(i, target-i)
        #     n = target - m
        #     comb_set.add(tuple((m,n)))
        
        # comb_list = list(comb_set)

        # idx1 = None
        # idx2 = None
        # for m,n in comb_list:
        #     # print(f"Combination:{(m,n)}")
        #     if m in nums_set:
        #         num1 = m
        #         num2 = target-m
        #         for i, num in enumerate(nums):
        #             if num1 == num and idx1 == None:
        #                 idx1 = i
        #                 # print(f"\tFound IDX1:{i} for num {num1}")
        #             elif num2 == num and idx2 == None:
        #                 idx2 = i
        #                 # print(f"\tFound IDX2:{i} for num {num2}")
        #             if not idx2 == None and not idx2 == None:
        #                 return [min(idx1, idx2), max(idx1, idx2)]
        #     idx1 = None
        #     idx2 = None


