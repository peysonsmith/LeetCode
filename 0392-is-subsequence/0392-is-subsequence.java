class Solution {
    public boolean isSubsequence(String s, String t) {
        // Char pointers
        int sPointer = 0;
        int tPointer = 0;

        // Base cases
        if (s.length() == 0) {
            return true;
        }
        if (s.length() > t.length()) {
            return false;
        }

        // Loop until the tPointer has reached the end of the word

        // If the s pointer reaches the end of the word and the last char
        // is equal to a character in t it means it is subs and return true

        // If the char at each pointer is pointing to the same letter shift
        // each pointer to the next letter
        // If they are not shift the tPointer until you find the same letter
        // or get to the end of t.
        while (tPointer < t.length()) {
            if (sPointer == s.length() - 1 && s.charAt(sPointer) == 
                t.charAt(tPointer)) {
                return true;
            }
            if (s.charAt(sPointer) == t.charAt(tPointer)) {
                sPointer++;
                tPointer++;
            } else {
                tPointer++;
            }
        }
        return false;
    }
}