class Solution:
    def findMin(self, nums: List[int]) -> int:

        # If front is greater  or equal than mid than: b = m. f += 1
        # If front is less than mid compare with back:
            # front > back: f = m + 1
            # front < back: return f
        # Run binary search using these conditions to cut the group in half each time (logn)
        
        f = 0
        b = len(nums) - 1

        while f < b:
            m = (f + b) // 2
            
            if nums[m] > nums[b]:
                f = m + 1
            else: 
                b = m
        
        return nums[f]
