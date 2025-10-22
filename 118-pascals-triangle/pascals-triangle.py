class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for r in range(numRows):
            curr_row = [1] * (r + 1)

            for c in range(1,r):
                curr_row[c] = triangle[r-1][c-1] + triangle[r-1][c]
            triangle.append(curr_row)
        return triangle