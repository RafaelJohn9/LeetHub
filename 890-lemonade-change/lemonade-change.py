class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] != 5:
            return False

        five_dollars: int = 0
        ten_dollars: int = 0

        for bill in bills:
            if bill == 5:
                five_dollars += 1
            elif bill == 10 and five_dollars > 0:
                five_dollars -= 1
                ten_dollars += 1
            elif bill == 20 and five_dollars > 0:
                if ten_dollars > 0:
                    five_dollars -= 1
                    ten_dollars -= 1
                elif five_dollars > 2:
                    five_dollars -= 3
                else:
                    return False
            else:
                return False
        
        return True