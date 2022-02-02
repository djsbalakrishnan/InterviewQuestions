class Solution:
	# @param A : string
	# @return an integer
	def solve(self, A):
        stack = []
        for ele in A:
            if len(stack) == 0:
                stack.append(ele)
            else:
                top = stack[len(stack) - 1]
                if ele == "}" and top == "{":
                    stack.pop()
                elif ele == "]" and top == "[":
                    stack.pop()
                elif ele == ")" and top == "(":
                    stack.pop()
                else:
                    stack.append(ele)
        
        if len(stack) == 0:
            return 1
        
        return 0
