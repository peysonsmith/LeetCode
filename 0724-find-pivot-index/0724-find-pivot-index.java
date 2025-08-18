class Solution {
    public int pivotIndex(int[] nums) {
        /* Create an array that has the sum of all the numbers in
         the array at that index. */
        int[] prefixSum = new int[nums.length];
        prefixSum[0] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            prefixSum[i] = prefixSum[i-1] + nums[i];
        }

        /* Base case: The sum of all the elements in the array to the
        right of the first number is 0*/
        if ((prefixSum[prefixSum.length - 1] - prefixSum[0]) == 0) {
            return 0;
        }

        /* Loop through the array starting at index 1 and check if
        the sum of the at the index before times 2 equals the final
        sum minus the number at the current pivot index*/
        for (int i = 1; i < prefixSum.length; i++) {
            if ((prefixSum[i-1] * 2) == (prefixSum[prefixSum.length - 1] - 
                nums[i])) {
                    return i;
                }
        }
        
        return -1;
    }
}