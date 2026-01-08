class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        # Check each character as the center of the longest palindrome
        for i in range(len(s)):
            # Odd palindrome
            p1 = i
            p2 = i
            while p1 >= 0 and p2 < len(s) and s[p1] == s[p2]:
                if (p2 - p1 + 1) > len(longest):
                    longest = s[p1:p2+1]
                p1 -= 1
                p2 += 1

            # Even palindrome
            p1 = i
            p2 = i + 1
            while p1 >= 0 and p2 < len(s) and s[p1] == s[p2]:
                if (p2 - p1 + 1) > len(longest):
                    longest = s[p1:p2+1]
                p1 -= 1
                p2 += 1 
        
        return longest
