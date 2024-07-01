class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for num in arr:
            if num % 2 != 0:
                count += 1
            elif count < 3:
                count = 0
        

        return True if count >= 3 else False