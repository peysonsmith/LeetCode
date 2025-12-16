class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # Create a stack. Add any elements in order from the array to the stack.
        # When an operation symbol appears pop the top element in the stack and
        # assign it to a temp variable.
        # Pop the next element on the top of the stack and operate it with the 
        # current operation and the temp variable and append it to the top of the stack.
        stack = []

        for token in tokens:
            if token in ['+','-','*','/']:
                t2 = stack.pop()
                t1 = stack.pop()
                if token == '+':
                    res = t1 + t2
                elif token == '-':
                    res = t1 - t2
                elif token == '*':
                    res = t1 * t2
                elif token == '/':
                    res = int(float(t1) / float(t2))

                stack.append(res)
            else:
                stack.append(int(token))

        return stack[-1]
                