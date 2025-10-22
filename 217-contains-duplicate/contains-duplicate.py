class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        for i in range(len(nums)):
            if nums[i] in hashSet:
                return True
            else:
                hashSet.add(nums[i])
        return False