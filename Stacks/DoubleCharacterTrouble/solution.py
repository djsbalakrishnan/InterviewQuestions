class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        stack = []
        for ele in A:
            if len(stack) == 0:
                stack.append(ele)
            else:
                top = stack[len(stack)-1]
                if ele == top:
                    stack.pop()
                else:
                    stack.append(ele)
        result = "".join(stack)
        return result

