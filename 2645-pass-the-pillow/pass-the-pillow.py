class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if n == 1:
            return 1
        
        current_person = 1
        direction = 1
        
        for _ in range(time):
            if current_person == 1 and direction == -1:
                direction = 1
            elif current_person == n and direction == 1:
                direction = -1
            
            current_person += direction
        
        return current_person
