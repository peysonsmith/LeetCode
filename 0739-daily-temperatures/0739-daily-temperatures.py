class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # Create a stack. Place element's position in stack if there are no elements in
        # the stack or if it is smaller than the top position's element. 
        # If an element comes up that is greater than one in the stack pop it and compare
        # the positions and put the difference in the answer array at the same position of
        # the element that was just popped. 
        # Keep doing this until an element in the stack is bigger or there are no more
        # elements in the stack. 
        # If there are no more elements to look at from the input array put 0 for the 
        # answer for the elements left in the stack at their positions
        stack = []
        answer = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                    pos = stack.pop()
                    answer[pos] = i - pos
            stack.append(i)

        return answer