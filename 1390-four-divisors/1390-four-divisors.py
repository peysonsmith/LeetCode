class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        # Go through each num in the array and check if divided by 1 to sqrt of the
        # of the num has a remainder of 0. If it does add the divisor and the complement
        # to the result. If there are more than 4 divisors break and dont add to res
        res = 0

        for num in nums:
            divisors = set()

            for j in range(1, (int(math.sqrt(num)) + 1)):
                if num % j == 0:
                    divisors.add(j)
                    divisors.add(num // j)

                    if len(divisors) > 4:
                        break

            if len(divisors) == 4:
                for d in divisors:
                    res += d

        return res