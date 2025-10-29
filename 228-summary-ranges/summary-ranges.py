class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0
        n = len(nums)
        while(i < n):
            begin = nums[i]
            j = i

            while j+1 < n and nums[j] == nums[j+1]-1:
                j+=1
            
            end = nums[j]
            if begin == end:
                ans.append(str(begin))
            else:
                ans.append(f"{begin}->{end}")
            
            i = j + 1
        
        return ans
        