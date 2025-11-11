class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        import sys
    # We use a set to keep track of the distinct maximums found so far
    # Using float('-inf') or None works well for Python
        m1 = m2 = m3 = float('-inf')

        for num in nums:
            # Skip duplicates if the number is already one of the top three
            if num == m1 or num == m2 or num == m3:
                continue
            
            # Update the maximums
            if num > m1:
                m3 = m2
                m2 = m1
                m1 = num
            elif num > m2:
                m3 = m2
                m2 = num
            elif num > m3:
                m3 = num
                
        # Check if a third distinct maximum was found
        # We can use float('-inf') as the initial value check
        if m3 == float('-inf'):
            # If not, return the maximum number (m1)
            return m1
        else:
            # Otherwise, return the third maximum (m3)
            return m3

