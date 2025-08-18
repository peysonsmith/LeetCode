class Solution {
    public int largestAltitude(int[] gain) {
        // Create an array with a size one bigger than gain that stores the
        // altitudes the hiker travels to starting at altitude 0.
        int[] altitudes = new int[gain.length + 1];
        altitudes[0] = 0;

        // Create variable that keeps track of the highest altitude
        int maxAlt = altitudes[0];

        // Loop through the gain array adding the element at each index to 
        // the previous altitude. Compare the current alitude to the highest
        // altitude.
        for (int i = 1; i <= gain.length; i++) {
            altitudes[i] = altitudes[i-1] + gain[i-1];

            if (altitudes[i] > maxAlt) {
                maxAlt = altitudes[i];
            }
        }

        return maxAlt;
    }
}