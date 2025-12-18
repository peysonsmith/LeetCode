class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        hi = len(nums) - 1
        lo = 0
        if nums[hi] == target:
            return hi
        if nums[lo] == target:
            return lo

        mid = (hi - lo) / 2

        while mid < hi and mid > lo:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid
            elif nums[mid] > target:
                hi = mid
            mid = lo + (hi - lo) / 2

        return -1
