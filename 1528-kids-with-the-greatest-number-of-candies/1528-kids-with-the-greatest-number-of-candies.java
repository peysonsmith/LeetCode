class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        // Use a loop to find the kid with most candies
        int mostCandies = 0;
        for (int i = 0; i < candies.length; i++) {
            if (candies[i] > mostCandies) {
                mostCandies = candies[i];
            }
        }

        // Create our boolean arraylist to keep track of if each kid meets
        // the requirement
        ArrayList<Boolean> result = new ArrayList<>();

        // Use another loop to go through and check each kid added with the 
        // extra candies has equal to or more than the kid with the most 
        // candies. 

        for (int i = 0; i < candies.length; i++) {
            if (candies[i] + extraCandies >= mostCandies) {
                result.add(true);
            } else {
                result.add(false);
            }
        }

        return result;   
    }
}