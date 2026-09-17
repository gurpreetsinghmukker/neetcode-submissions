class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if temperatures==sorted(temperatures,reverse=True):
            return [0]*len(temperatures)
        stack_idx = []
        result = [0]*len(temperatures)
        for idx, t in enumerate(temperatures):
            while len(stack_idx) > 0  and temperatures[idx]>temperatures[stack_idx[-1]]:
                p_idx = stack_idx.pop()
                result[p_idx] = idx - p_idx
            stack_idx.append(idx)
        return result
        