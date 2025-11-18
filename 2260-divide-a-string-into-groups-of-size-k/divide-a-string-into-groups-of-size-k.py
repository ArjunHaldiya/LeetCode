class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        n = len(s)
        i=0
        if n%k == 0:
            while i < n:
                res.append((s[i:(i+k)]))
                i = i + k
        else:
            s = s + fill*(k-1)
            while i <= n:
                res.append((s[i:(i+k)]))
                i = i+k
        return res

