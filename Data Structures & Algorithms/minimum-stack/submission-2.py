class MinStack:

    def __init__(self):

        self.num_stack = []
        self.min_idx_stack = []
        self.min_num = float('inf')
        self.min_idx = 0
    def push(self, val: int) -> None:
        if val < self.min_num:
            self.min_num = val
            self.min_idx = len(self.num_stack)
        self.num_stack.append(val)
        self.min_idx_stack.append(self.min_idx)

    def pop(self) -> None:

        if self.num_stack:
            self.num_stack.pop()
            self.min_idx_stack.pop()
        
        if self.num_stack:
            self.min_idx = self.min_idx_stack[-1]
            self.min_num = self.num_stack[self.min_idx]
        else:
            self.min_num = float('inf')
            self.min_idx = 0


        

    def top(self) -> int:
        return self.num_stack[-1]

    def getMin(self) -> int:
        return self.min_num
        
