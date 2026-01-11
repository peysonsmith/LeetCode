class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        for i in range(len(nums)):
            # Edge case: If nums[i] and nums[i - 1] are duplicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            f = i + 1
            b = len(nums) - 1
            target = 0 - nums[i]

            while f < b:
                if nums[f] + nums[b] > target:
                    b -= 1
                elif nums[f] + nums[b] < target:
                    f += 1
                else:
                    res.append([nums[i], nums[f], nums[b]])
                    f += 1
                    b -= 1

                    while f < b and nums[f] == nums[f - 1]:
                        f += 1
                    while f < b and nums[b] == nums[b + 1]:
                        b -= 1

        return res

