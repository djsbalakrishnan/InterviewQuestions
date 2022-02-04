class Solution:
	# @param A : list of strings
	# @return an integer
    def calculate(self, op1, op2, operator):
        if operator == "+":
            return int(op1) + int(op2)
        elif operator == "*":
            return int(op1) * int(op2)
        elif operator == "-":
            return int(op1) - int(op2)
        else:
            return int(op1) // int(op2)

	def evalRPN(self, A):
        ex_stack = []
        for ele in A:
            if ele in ["+", "*", "/", "-"]:
                op2 = ex_stack.pop()
                op1 = ex_stack.pop()
                operator = ele
                result = self.calculate(op1, op2, operator)
                ex_stack.append(result)
            else:
                ex_stack.append(ele)
        
        return ex_stack[len(ex_stack)-1]
