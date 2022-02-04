class Solution:
    # @param A : list of integers
    # @return an integer
    def NSL(self, A):
        nsl = [-1]
        stack = [0]
        for i in range(1, len(A)):
            ele = A[i]
            while len(stack) > 0 and ele <= A[stack[-1]]:
                stack.pop()
            if len(stack) > 0:
                nsl.append(stack[-1])
            else:
                nsl.append(-1)
            stack.append(i)
        
        return nsl
    
    def NSR(self, A):
        nsr = [len(A)]*len(A)
        stack = [len(A)-1]
        for i in range(len(A)-2, -1, -1):
            ele = A[i]
            while len(stack) > 0 and ele <= A[stack[-1]]:
                stack.pop()
            if len(stack) > 0:
                nsr[i] = stack[-1]
            else:
                nsr[i] = len(A)
            stack.append(i)
        
        return nsr

    def NLL(self, A):
        nll = [-1]*len(A)
        stack = [0]
        for i in range(1, len(A)):
            ele = A[i]
            while len(stack) > 0 and ele >= A[stack[-1]]:
                stack.pop()
            if len(stack) > 0:
                nll[i] = stack[-1]
            else:
                nll[i] = -1
            stack.append(i)
        
        return nll
    
    def NLR(self, A):
        nlr = [len(A)]*len(A)
        stack = [len(A)-1]
        for i in range(len(A)-2, -1, -1):
            ele = A[i]
            while len(stack) > 0 and ele >= A[stack[-1]]:
                stack.pop()
            if len(stack) > 0:
                nlr[i] = stack[-1]
            else:
                nlr[i] = len(A)
            stack.append(i)
        
        return nlr

    def solve(self, A):
        MOD = 1e9+7
        nsl = self.NSL(A)
        nsr = self.NSR(A)
        nll = self.NLL(A)
        nlr = self.NLR(A)
        contribution = 0

        for i in range(len(A)):
            contribution = ((contribution%MOD) + ((A[i]*((i-nll[i])*(nlr[i]-i)))%MOD))%MOD
            contribution = contribution - (A[i]*((i-nsl[i])*(nsr[i]-i)))
        
        return int(contribution)
