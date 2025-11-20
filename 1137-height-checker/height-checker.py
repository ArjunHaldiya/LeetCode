class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        expected = sorted(heights)
        n = len(heights)
        count = 0

        for i in range(n):
            if heights[i] != expected[i]:
                count+=1

        return count 