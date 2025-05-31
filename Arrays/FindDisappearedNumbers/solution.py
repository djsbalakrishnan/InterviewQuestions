class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        for i in range(n):
            val = abs(nums[i])
            # mark number at index (val-1) as negative 
            if nums[val-1] > 0:
                nums[val-1] *= -1
        
        for i in range(n):
            if nums[i] > 0:
                ans.append(i+1)
        
        return ans
