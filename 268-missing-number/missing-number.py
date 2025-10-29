class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       n = len(nums)
       expected_sum = n*(n+1)//2
       act_sum = sum(nums)
       return expected_sum - act_sum
       
            