class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = [None] * (len(nums) * 2)

        for i in range(len(nums)):
            res[i] = nums[i]

        j = len(nums)
        for i in range(len(nums)):
            res[j] = nums[i]
            j += 1

        return res