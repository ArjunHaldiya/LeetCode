class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        return nums[len(nums)//2]
