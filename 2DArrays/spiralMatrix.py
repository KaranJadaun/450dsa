class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, down, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1 
        direc, arr = 0, []
        while (top <= down and left <= right):
            if (direc == 0):
                for i in range(left, right + 1): arr.append(matrix[top][i])
                top += 1
            elif (direc == 1):
                for i in range(top, down + 1): arr.append(matrix[i][right])
                right -= 1
            elif (direc == 2):
                for i in range(right, left - 1, -1): arr.append(matrix[down][i])
                down -= 1
            else:
                for i in range(down, top - 1, -1): arr.append(matrix[i][left])
                left += 1
            direc = (direc + 1) % 4
        return arr
