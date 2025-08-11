class Solution {
    public void moveZeroes(int[] nums) {
        // Have a pointer that points to the position of zeros and one that
        // finds the positions of non zeros. Loop through the array and if
        // the number is non zero switch it with the zero and update the 
        // left pointer
        int left = 0;
        int right = 1;

        //base case nums length is 1
        if (nums.length < 2) {
            return;
        }
        
        // Check if the left pointer is pointing at a zero or move both
        // pointers one to the right
        // If left pointer is 0 and right pointer is 0 move the right
        // pointer one to the right
        // Else case: the left pointer is on a zero and the right pointer is
        // on a non-zero. Swap the two integers;
        while (right < nums.length) {
            if (nums[left] != 0) {
                left++;
                right++;
            } else if (nums[right] == 0) {
                right++;
            } else {
                nums[left] = nums[right];
                nums[right] = 0;
            }
        }
    }
}