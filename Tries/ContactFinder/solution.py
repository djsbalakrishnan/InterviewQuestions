class Trie:
    def __init__(self, letter):
        self.val = letter
        self.next = [None]*26
        self.prefix_count = 0


class Solution:
    # @param A : list of integers
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        root = Trie("")
        result = []
        for i in range(len(A)):
            value_a = A[i]
            value_b = B[i]
            curr = root
            flag = True

            if value_a == 0:
                for letter in value_b:
                    curr.prefix_count = curr.prefix_count + 1
                    index = ord(letter) - ord('a')
                    if curr.next[index] is None:
                        node = Trie(letter)
                        curr.next[index] = node
                    curr = curr.next[index]
                curr.prefix_count += 1
            
            if value_a == 1:
                for letter in value_b:
                    index = ord(letter) - ord('a')
                    if curr.next[index] is None:
                        flag = False
                        break
                    curr = curr.next[index]
                if flag:
                    result.append(curr.prefix_count)
                else:
                    result.append(0)
        
        return result
