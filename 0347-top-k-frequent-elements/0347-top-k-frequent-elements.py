class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Create a hashmap
        count = {}

        # Put each integer in the nums array as the key and count the number of times 
        # it shows up and add one to the value.
        # If the key does not already exist use get and initialize it to value 0/
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Use a bucket sort where each element in the ith array shows up i number of times
        # Set number of frequencies to the len of nums plus 1
        freq = [[] for i in range(len(nums) + 1)]

        # We know in our count the key represents the integer and the value represents the
        # number of times it shows up.
        # We are going to go through each key-value pair and append the key to the
        # array positioned in the value spot
        for key, val in count.items():
            freq[val].append(key)

        output = []

        # Iterate through the array of arrays in decending order and append each int
        # to our output until we have k values
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                output.append(j)
                if len(output) == k:
                    return output
