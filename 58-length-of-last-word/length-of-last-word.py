class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if(len(s.strip()) < 2):
            return len(s.strip())
        else:
            newS = s.strip()[::-1]
            spaceIndex = newS.find(" ")
            if(spaceIndex == -1):
                return len(newS)

        return spaceIndex