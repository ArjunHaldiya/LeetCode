class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if not bits: return null

        n = len(bits)
        i = 0

        while i < n-1:
            if bits[i] == 0:
                i += 1
            else:
                i+= 2

        return i == n-1