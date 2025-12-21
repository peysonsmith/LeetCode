class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1. Use binary search to set front, back, and mid
        # 2. Check if mid is in the left sorted array or right sorted
        #       - Is in left if mid >= front
        #       - In right else
        # 3. If mid is in left all elements to left are smaller
        #    If mid is in right all elements to right are greater
        #    So check if target is left of mid or right or equal
        f = 0
        b = len(nums) - 1

        while f <= b:
            m = (f + b) // 2

            # Base case check if mid is the target
            if nums[m] == target:
                return m

            # Mid is in left sorted array
            if nums[m] >= nums[f]:
                if target < nums[m] and target >= nums[f]:
                    b = m - 1
                else:
                    f = m + 1
                
            else: # Mid is in right sorted array
                if target > nums[m] and target <= nums[b]:
                    f = m + 1
                else:
                    b = m - 1
        
        return -1