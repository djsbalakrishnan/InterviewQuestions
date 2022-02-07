class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer

    def find_pivot(self, arr, start, end):
        if start > end:
            return -1
        
        mid = (start + end) // 2
        if mid < end and arr[mid] > arr[mid + 1]:
            return mid
        elif mid > start and arr[mid] < arr[mid-1]:
            return mid - 1
        elif arr[start] < arr[mid]:
            start = mid + 1
            return self.find_pivot(arr, start, end)
        else:
            end = mid - 1
            return self.find_pivot(arr, start, end)
    

    def b_search(self, arr, start, end, val):
        if start > end:
            return -1
        
        mid = (start + end) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] > val:
            end = mid - 1
            return self.b_search(arr, start, end, val)
        else:
            start = mid + 1
            return self.b_search(arr, start, end, val)


    def search(self, A, B):
        # find the pivot value 
        # do the binary search in 2 arrays
        pivot = self.find_pivot(A, 0, len(A)-1)
        ans = -1
        if pivot != -1:
            ans = self.b_search(A, 0, pivot, B)
            if ans == -1:
                return self.b_search(A, pivot + 1, len(A)-1, B)
            else:
                return ans
        else:
            return self.b_search(A, 0, len(A)-1, B)
