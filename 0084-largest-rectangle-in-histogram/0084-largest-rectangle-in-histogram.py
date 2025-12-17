class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # 1. For every element, add to index to stack if the stack is empty or if it is 
        #    greater than the top element.
        # 2. If it is not greater, pop the top element, multiply it by (curr_i - top_i)
        #    and compare it to current largest
        # 3. Continue to check until it is greater than an element in the stack or the
        #    stack is empty
        # 4. Set the edge to the index of the last element. For each of the remaining
        #    elements in the stack pop the element and store it in a temp var. Do
        #    (edge - position) * heights[position] and compare to largest
        stack = []
        largest = 0

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                temp = stack.pop()
                # Calculate width at that point
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1

                largest = max(largest, (heights[temp] * width))
            
            stack.append(i)

        while stack:
            temp = stack.pop()
            
            if not stack:
                width = len(heights)  # Full width!
            else:
                width = len(heights) - stack[-1] - 1
            
            largest = max(largest, heights[temp] * width)

        return largest