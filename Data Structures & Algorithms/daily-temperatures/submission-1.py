class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack_t = []
        stack_idx = []
        result = [0]*len(temperatures)

        for idx, t in enumerate(temperatures):
            # print(f"{idx} - {stack_t}")
            while True:
                if len(stack_t) < 1:
                    # print('h')
                    break
                if temperatures[idx]>stack_t[-1]:
                    # print("h1")
                    stack_t.pop()
                    p_idx = stack_idx.pop()
                    result[p_idx] = idx - p_idx
                else:
                    # print("h2")
                    break
            stack_t.append(t)
            stack_idx.append(idx)
        return result
        