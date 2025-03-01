class Solution:
    def isHappy(self, n: int) -> bool:
        fast = slow = n

        get_next = lambda x: sum([int(y)**2 for y in str(x)])

        fast = get_next(get_next(fast))
        slow = get_next(slow)
        
        while fast != slow and fast != 1:
            fast = get_next(get_next(fast))
            slow = get_next(slow)
        
        if fast == 1:
            return True
        
        return False