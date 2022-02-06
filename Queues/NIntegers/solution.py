class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A):
        if A == 1:
            return [1]
        if A == 2:
            return [1,2]
        
        queue = [-1]*A
        queue[0], queue[1], queue[2] = 1, 2, 3
        options = [1,2,3]
        index = 3

        while index < A:
            queue[index] = queue[((index//3)-1)]*10 + options[int(index%3)]
            index += 1
        
        return queue
