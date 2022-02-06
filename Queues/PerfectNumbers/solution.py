from collections import deque

class Solution:
    def solve(self, A):
        q = deque()
        q.append("1")
        q.append("2")
        ans = []
        while len(ans) < A:
            val = q.popleft()
            ans.append(val+val[::-1])
            f = val + "1"
            s = val + "2"
            f_d = f[::-1]
            s_d = f[::-1]
            q.append(f)
            q.append(s)
        
        return ans[A-1]
