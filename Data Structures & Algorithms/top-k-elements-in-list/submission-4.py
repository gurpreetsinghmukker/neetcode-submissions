from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq_dict = defaultdict(int)
        for num in nums:
            num_freq_dict[num] += 1
        sorted_pairs = sorted([(k,v) for k,v in num_freq_dict.items()], key=lambda x:x[1], reverse=True) 
        return [k for k,v in sorted_pairs[:k]]