class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Find largest int
        maxB = 0
        for b in piles:
            if b > maxB:
                maxB = b

        # Binary search for correct k
        lo = 1
        hi = maxB
        k = 0

        while lo <= hi:
            mid = (hi + lo) // 2
            hours = 0

            # Find total hours using mid k
            for b in piles:
                hours += math.ceil(b / mid)

            if hours <= h:
                k = mid
                hi = mid - 1
            elif hours > h:
                lo = mid + 1

        return k

