class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        # 1. Create pairs with position and then speed using zip
        # 2. Sort pairs by position in reverse order
        # 3. For each pair in that order calculate number of units it will take to reach
        #    target and put on top of stack if empty or greater than top
        # 4. Empty stack and count elements to see how many fleets there are and return
        pairs = zip(position, speed)

        sort_Pairs = sorted(pairs, reverse=True)

        stack = []
        for i in range(len(sort_Pairs)):
            units_Away = (target - sort_Pairs[i][0]) / float(sort_Pairs[i][1])
            if not stack:
                stack.append(units_Away)
            elif units_Away > stack[-1]:
                stack.append(units_Away)

        return len(stack)



        
        