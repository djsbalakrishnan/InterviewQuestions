class Trie:
    def __init__(self, letter):
        self.val = letter
        self.next = [None]*26
        self.is_end = False


class Solution:
    # @param A : list of strings
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        root = Trie("")
        result = []
        for word in A:
            curr = root
            for letter in word:
                index = ord(letter) - ord('a')
                if curr.next[index] is None:
                    node = Trie(letter)
                    curr.next[index] = node
                curr = curr.next[index]
            curr.is_end = True
        
        for word in B:
            curr = root
            flag = True
            for letter in word:
                index = ord(letter) - ord('a')
                if curr.next[index] is None:
                    flag = False
                    break
                curr = curr.next[index]
            if curr.is_end and flag:
                result.append(1)
            else:
                result.append(0)
        
        return result
