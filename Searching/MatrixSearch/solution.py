class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer

    def binary_search(self, arr, start, end, val):
        if start > end: 
            return 0
        
        mid = (start + end) // 2
        if arr[mid] == val:
            return 1
        elif arr[mid] > val:
            end = mid - 1
            return self.binary_search(arr, start, end, val)
        else:
            start = mid + 1
            return self.binary_search(arr, start, end, val)

    def searchMatrix(self, A, B):
        # Check for first and last element of each row and check if the number lies in the range 
        for row in A:
            first_ele = row[0]
            last_ele = row[-1]
            if first_ele <= B and last_ele >= B:
                return self.binary_search(row, 0, len(row)-1, B)
        
        return 0
