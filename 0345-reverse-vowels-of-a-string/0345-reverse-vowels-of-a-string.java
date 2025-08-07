class Solution {
    public String reverseVowels(String s) {
        // Base case if s length is 1 return
        if (s.length() <= 1) {
            return s;
        }

        // Create a hashmap with all the vowels
        HashMap<Character, Integer> vowels = new HashMap<>();
        String tempVowels = "AaEeIiOoUu";
        for (int i = 0; i < tempVowels.length(); i++) {
            vowels.put(tempVowels.charAt(i), i);
        }

        // Turn word into a char array.
        char[] word = s.toCharArray();
        
        // Create two pointers that start at the start and end characters
        int left = 0;
        int right = s.length() - 1;

        // Loop until the left pointer position is greater than or equal to
        // the right pointer position.
        // Check if the left pointer char is a vowel. If not move left
        // pointer one to the right.
        // Check if the right pointer char is a vowel. If not move right
        // pointer one to the left.
        // If both point at a vowel swap characters.
        while (left < right) {
            if (!vowels.containsKey(s.charAt(left))) {
                left++;
            } else if (!vowels.containsKey(s.charAt(right))) {
                right--;
            } else {
                char temp = word[left];
                word[left] =  word[right];
                word[right] = temp;
                left++;
                right--;
            }
        }

        // Turn char array back into a string a return
        String result = new String(word);
        return result;
    }
}