class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if (m * k) > len(bloomDay):
            return -1
        
        def canMakeBonquets(days: int) -> bool:
            flowers = 0
            bonquets = 0

            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1

                    if flowers >= k:
                        bonquets += 1
                        flowers = 0
                else:
                    flowers = 0
            if bonquets >= m:
                return True

            return False
        
        left, right = min(bloomDay), max(bloomDay)

        while left < right:
            mid = (left + right) // 2

            if canMakeBonquets(mid):
                right = mid
            else:
                left = mid + 1
        
        return left if canMakeBonquets(left) else -1