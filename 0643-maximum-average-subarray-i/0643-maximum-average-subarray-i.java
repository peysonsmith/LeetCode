class Solution {
    public double findMaxAverage(int[] nums, int k) {
        // Create pointers pointing at the start of the array up to the kth
        int i = 0;
        int j = k - 1;

        // Create a count and maximum average variables
        int count = 0;
        double maxAvg = Double.NEGATIVE_INFINITY;

        // Loop adding up the original range to count
        for (int l = 0; l < j; l++) {
            count += nums[l];
        }

        // Loop through the array until the j pointer has reached the end of
        // array
        // Divide count by k and compare it to the maximum average. 
        // Subtract the element moving out of the range and add the number
        // entering the range to the count. Move pointers.
        while (j < nums.length) {
            count += nums[j];
            double average = ((double) count) / k;

            if (average > maxAvg) {
                maxAvg = average;
            }

            j++;
            count -= nums[i];
            i++;
        }

        return maxAvg;
    }
}