class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles
        while numBottles >= numExchange:
            bottlesGot = numBottles // numExchange
            numBottles -= (bottlesGot * numExchange)
            numBottles += bottlesGot
            result += bottlesGot
        return result