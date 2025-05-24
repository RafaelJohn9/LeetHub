class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        radius = 0
        j = 0

        for house in houses:
            while j + 1 < len(heaters) and abs(heaters[j + 1] - house) <= abs(heaters[j] - house):
                j += 1
            
            distance = abs(heaters[j] -house)
            radius = max(radius,distance)
        

        return radius