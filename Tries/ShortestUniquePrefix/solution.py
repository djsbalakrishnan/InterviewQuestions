class Trie:
    def __init__(self, letter):
        self.val = letter
        self.next = [None]*26
        self.prefix_count = 0

class Solution:
	# @param A : list of strings
	# @return a list of strings
	def prefix(self, A):
        root = Trie("")
        result = []
        for word in A:
            curr = root
            for letter in word:
                curr.prefix_count = curr.prefix_count + 1
                index = ord(letter) - ord('a')
                if curr.next[index] is None:
                    node = Trie(letter)
                    curr.next[index] = node
                curr = curr.next[index]
            curr.prefix_count += 1

        for word in A:
            curr = root
            unique_prefix = []
            flag = True
            for letter in word:
                unique_prefix.append(curr.val)
                if curr.prefix_count == 1:
                    flag = False
                    break
                else:
                    index = ord(letter) - ord('a')
                    curr = curr.next[index]
            if flag:
                unique_prefix.append(curr.val)
            result.append("".join(unique_prefix[1:]))
        
        return result
