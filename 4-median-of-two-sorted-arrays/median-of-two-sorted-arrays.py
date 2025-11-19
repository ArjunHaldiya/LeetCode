class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums = sorted(nums)
        n = len(nums)
        mid = int(n/2)

        if n%2 == 0:
            return (nums[mid] + nums[(mid - 1)])/2
        else:
            return nums[mid]