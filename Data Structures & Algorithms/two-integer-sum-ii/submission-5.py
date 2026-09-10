from collections import defaultdict
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers)-1
        sum = numbers[l]+numbers[r]
        while True:
            if sum<target:
                l=l+1
            elif sum >target:
                r = r-1
            else:
                return [l+1,r+1]
            sum = numbers[l]+numbers[r]
        