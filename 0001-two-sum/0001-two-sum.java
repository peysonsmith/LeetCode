class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Create a hashmap 
        HashMap<Integer, Integer> checkNum = new HashMap<>();

        // Go through each element of the array
        // Subtract the current element from the target to get new target
        // If the map contains this new target return the postion of each
        // Otherwise add that number and target to hashmap
        for (int i = 0; i < nums.length; i++) {
            int newTarget = target - nums[i];

            if (checkNum.containsKey(newTarget)) {
                return new int[]{checkNum.get(newTarget), i};
            }

            checkNum.put(nums[i], i);
        }

    return nums;
    }
}