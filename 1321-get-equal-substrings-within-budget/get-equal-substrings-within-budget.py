class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        cost = [abs(ord(s[i]) - ord(t[i])) for i in range(n)]

        max_length = 0
        current_cost = 0
        left = 0

        for right in range(n):
            current_cost += cost[right]
            
            while current_cost > maxCost:
                current_cost -= cost[left]
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length
