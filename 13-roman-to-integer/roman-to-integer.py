class Solution:
    def romanToInt(self, s: str) -> int:
        romanMap = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }

        total = 0
        n = len(s)

        for i in range(n-1):
            currVal = romanMap[s[i]]
            nextVal = romanMap[s[i+1]]

            if currVal < nextVal:
                total -= currVal

            else:
                total += currVal
            
        total +=romanMap[s[-1]]

        return total
