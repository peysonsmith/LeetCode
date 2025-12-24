class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Make sure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        # 1. We need to find the left half of the "merged array"
        # Divide total number of items by 2 and round down and thats how many elements
        # in our left partition
        total_ele = len(nums1) + len(nums2)
        half = (total_ele + 1) // 2
        
        # 2. Binary search to mid point of nums1
        f = 0
        b = len(nums1)  # Should be len, not len - 1
        
        while f <= b:
            m = (f + b) // 2  # Number of elements from nums1 in left partition
            
            # 3. Take half - m to find how many elements from nums2 in left partition
            i = half - m
            
            # Get boundary values
            nums1_left = nums1[m - 1] if m > 0 else float('-inf')
            nums2_left = nums2[i - 1] if i > 0 else float('-inf')
            
            nums1_right = nums1[m] if m < len(nums1) else float('inf')
            nums2_right = nums2[i] if i < len(nums2) else float('inf')
            
            # Check if we have a valid partition
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # Found correct partition!
                if total_ele % 2 == 1:
                    # Odd: return max of left partition
                    return max(nums1_left, nums2_left)
                else:
                    # Even: return average of middle two elements
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            
            elif nums1_left > nums2_right:
                # Too many elements from nums1 in left partition
                b = m - 1
            else:
                # Too few elements from nums1 in left partition
                f = m + 1