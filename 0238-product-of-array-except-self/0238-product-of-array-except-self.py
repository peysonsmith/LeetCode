class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Use a prefix and postfix approach without using extra memory
        output = [0] * len(nums)
        counter = 1
        
        # Prefix - Put the product of all previous nums in output array
        for i in range(len(nums)):
            if i == 0: # Edge case
                output[0] = 1
                counter = 1
            else:
                output[i] = counter * nums[i-1]
                counter = output[i]
        print(output)
        
        # Reset counter
        counter = 0

        # Postfix - Multiply prefix by product of all nums after
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                output[i] = output[i]
                counter = nums[i]
            else:
                output[i] = output[i] * counter
                counter = counter * nums[i]

        return output