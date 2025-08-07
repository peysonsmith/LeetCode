class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        // Go through the array linearly and if it is a 0, check if the
        // flower before and after it are also zero. Edge cases are i = 0 and
        // i = flowerbed.length
        for (int i = 0; i < flowerbed.length; i++) {
            if (flowerbed[i] == 0 && (i == 0 || flowerbed[i-1] == 0) && 
                (i  == flowerbed.length - 1 || flowerbed[i+1] == 0)) {
                    flowerbed[i] = 1;
                    n--;
                }
        }

        if (n <= 0) {
            return true;
        }

        return false;
    }
}