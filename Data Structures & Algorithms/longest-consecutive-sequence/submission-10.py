from collections import defaultdict, deque
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sorted_nums = sorted(nums)
        curr_seq = 1
        longest_seq = 1
        last_num = sorted_nums[0]
        # print(f"{sorted_nums}")
        for num in sorted_nums[1:]:
            # if not curr_seq:
            #     curr_seq = 1
            #     longest_seq = max(longest_seq, curr_seq)
            #     last_num = num
            #     print(f"{num}-{curr_seq}")
            # else:
            if num == last_num+1:
                curr_seq = curr_seq +1
                longest_seq = max(longest_seq, curr_seq)
                last_num = num
            elif num == last_num:
                continue
            else:
                curr_seq = 1
                last_num = num

            # print(f"{num}-{curr_seq}")
        return longest_seq