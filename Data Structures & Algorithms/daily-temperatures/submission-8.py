class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack_t = []
        stack_idx = []
        result = [0]*len(temperatures)

        for idx, t in enumerate(temperatures):
            # print(f"{idx} - {stack_t}")
            while len(stack_idx) > 0  and temperatures[idx]>temperatures[stack_idx[-1]]:
                # if len(stack_idx) < 1:
                #     break
                # if temperatures[idx]>temperatures[stack_idx[-1]]:
                p_idx = stack_idx.pop()
                result[p_idx] = idx - p_idx
                # else:
                #     break
            stack_idx.append(idx)
        return result
        