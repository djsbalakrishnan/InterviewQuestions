class Solution:
	# @param A : string
	# @return a strings
	def simplifyPath(self, A):
        stack = []
        A = A.split("/")
        for ele in A:
            if ele == "" or ele == ".":
                pass
            elif ele == ".." and len(stack) > 0:
                stack.pop()
            elif ele == ".." and len(stack) == 0:
                pass 
            else:
                stack.append(ele)
        result = "/" + "/".join(stack)
        return result
