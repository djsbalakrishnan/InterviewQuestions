class Solution:
    def solve(self, A, B, C):
        stack = [B]
        for ele in C:
            if ele == 0:
                stack.pop()
            else:
                stack.append(ele)
        return stack[len(stack)-1]
