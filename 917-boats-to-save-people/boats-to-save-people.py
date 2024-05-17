class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        boats = 0
    
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1  # they can share a boat
            right -= 1  # heaviest person always goes
            boats += 1  # one boat is used
    
        return boats