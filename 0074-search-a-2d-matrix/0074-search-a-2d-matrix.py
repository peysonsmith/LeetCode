class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 1. Binary search through first column to find correct row. We know we have found
        #    the correct row once the first element in the row is smaller than the target
        #    and the last element in the row is greater than the last element.
        # 2. Then use a binary search on that row to find target.
        loRow = 0
        hiRow = len(matrix) - 1
        keyRow = -1

        # Binary search to find correct row
        while loRow <= hiRow:
            midRow = (loRow + hiRow) // 2
            if matrix[midRow][0] > target:
                hiRow = midRow - 1
            elif matrix[midRow][0] < target and matrix[midRow][len(matrix[0]) - 1] < target:
                loRow = midRow + 1
            elif matrix[midRow][0] == target or matrix[midRow][len(matrix[0]) -1] == target:
                return True
            elif matrix[midRow][0] < target and matrix[midRow][len(matrix[0]) - 1] > target:
                keyRow = midRow
                break

        if keyRow == -1:
            return False

        # Binary search using correct row to find if element exists
        lo = 0
        hi = len(matrix[0]) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[keyRow][mid] == target:
                return True
            elif matrix[keyRow][mid] > target:
                hi = mid - 1
            elif matrix[keyRow][mid] < target:
                lo = mid + 1

        return False