class MinStack:
    def __init__(self): 
        self.stack = []
        self.min_stack = []
        self.curr_min = 1e9 + 9
    def push(self, x):
        m = min(x, self.curr_min)
        self.curr_min = m
        self.min_stack.append(m)
        self.stack.append(x)
    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()
            self.min_stack.pop()
            if len(self.min_stack) > 0:
                self.curr_min = self.min_stack[len(self.min_stack) - 1]
            else:
                self.curr_min = 1e9 + 9
    def top(self):
        if len(self.stack) > 0:
            t = self.stack[len(self.stack) - 1]
            return t
        else:
            return -1
    def getMin(self):
        if len(self.min_stack) > 0:
            m = self.min_stack[len(self.min_stack) - 1]
            return m
        else:
            return -1
