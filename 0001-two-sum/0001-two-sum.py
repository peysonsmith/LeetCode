class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}

        for i in range(len(nums)):
            target_pair = target - nums[i]
            if target_pair in map:
                return [map.get(target_pair), i]
            else:
                map[nums[i]] = i

        