class MinStack:

    def __init__(self):
        self.stack = []
        self.curr_min = 2**(+31)
        self.min_stack = [2**(+31)]
        return None
    def push(self, val: int) -> None:
        if not type(1) == type(val):
            return None
        self.stack.append(val)
        self.curr_min = min(self.curr_min, val)
        self.min_stack.append(self.curr_min)
        return None
    def pop(self) -> None:
        self.min_stack.pop()
        self.stack.pop()
        self.curr_min = self.min_stack[-1]
        # print(self.min_stack)
        return None
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.curr_min
        
