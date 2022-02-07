class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    def binary_search_ceil(self, arr, left, right, val):
        if left > right:
            return left
                
        mid = (left + right)//2
        if arr[mid] == val:
            return mid
        
        elif arr[mid] > val:
            right = mid - 1
            return self.binary_search_ceil(arr, left, right, val)
        
        else:
            left = mid + 1
            return self.binary_search_ceil(arr, left, right, val)


    def searchInsert(self, A, B):
        # find the ceil 
        return self.binary_search_ceil(A, 0, len(A)-1, B)
