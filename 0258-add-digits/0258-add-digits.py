class Solution:
    def addDigits(self, num: int) -> int:
        str_num = str(num)

        while len(str_num) > 1:
            num = 0
            for dig in str_num:
                num += int(dig)
            
            str_num = str(num)

        return num

        
