import collections
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = collections.Counter(arr)
        res = []
        arr = sorted(arr)
        for i in range(len(arr)):
            if counter[arr[i]] == arr[i]:
                res.append(arr[i])

        if len(res) > 1:
            return res[len(res) - 1]

        if counter[1] == 1:
            return 1


        return -1