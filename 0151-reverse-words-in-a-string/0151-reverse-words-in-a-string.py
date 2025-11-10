class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Convert string to list
        str_list = list(s)

        # Create a helper method that switches all of the characters in a string
        def flipString(s, starti, endi):
            front = starti
            back = endi
            temp = ''
            for i in range((endi - starti + 1) // 2):
                temp = s[front]
                s[front] = s[back]
                s[back] = temp
                front += 1
                back -= 1
            return s

        # Flip the characters in our starting string
        str = flipString(str_list, 0, len(s) - 1)

        # A pointer keeping track of original position and one searching for a space
        p1 = 0
        p2 = 0
        while p2 < len(str_list):
            if str_list[p2] == ' ':
                flipString(str_list, p1, p2 - 1)
                p2 += 1
                p1 = p2
            else:
                p2 += 1
        
        # Flip the last word (no space after it)
        str_list = flipString(str_list, p1, len(str_list) - 1)

        # Check for initial space(s), multispaces, or end space(s)
        while str_list[0] == ' ':
            str_list.pop(0)

        end = len(str_list) - 1
        while str_list[end] == ' ':
            str_list.pop(end)
            end -= 1

        i = 0
        while i < len(str_list) - 1:
            if str_list[i] == ' ' and str_list[i + 1] == ' ':
                str_list.pop(i + 1)
            else:
                i += 1 

        return ''.join(str_list)

        

