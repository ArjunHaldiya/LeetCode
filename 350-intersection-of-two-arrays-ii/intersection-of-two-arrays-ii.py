import collections
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Optimize by ensuring nums1 is the smaller array for building the counter
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # Create a frequency map for elements in nums1
        freq_map = collections.Counter(nums1)
        
        result = []
        # Iterate through nums2 and check for common elements
        for num in nums2:
            if freq_map[num] > 0:
                result.append(num)
                freq_map[num] -= 1  # Decrement count to handle duplicates
        
        return result