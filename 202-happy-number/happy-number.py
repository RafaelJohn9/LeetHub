class Solution:
    def isHappy(self, n: int) -> bool:
        backtrack = {}

        num = n
        while num != 1:
            backtrack[num] = True

            num = sum([int(digit)**2 for digit  in str(num)])
            
            if backtrack.get(num, False):
                return False
        
        return  True