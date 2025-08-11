class Solution {
    public int maxVowels(String s, int k) {
        // Have a current vowel counter and a string with all of the vowels
        int currVowels = 0;
        String vowels = "aeiou";
        char[] charArray = s.toCharArray();

        // Check how many of the first k letters letters are vowels and update the maxVowels
        for (int i = 0; i < k; i++) {
            if (vowels.contains(String.valueOf(charArray[i]))) {
                currVowels++;
            }
        }

        // Create a current vowels counter
        int maxVowels = currVowels;

        // Check if the letter leaving the window is a vowel and subtract one from current
        // vowels. If the character being added to the window is a vowel add one to the
        // current count and compare it to maxVowels.
        for (int i = k; i < s.length(); i++) {
            if (vowels.contains(String.valueOf(charArray[i-k]))) {
                currVowels--;
            }

            if (vowels.contains(String.valueOf(charArray[i]))) {
                currVowels++;
            }

            maxVowels = Math.max(maxVowels, currVowels);

            // rightP++;
        }
        
        return maxVowels;
    }
}