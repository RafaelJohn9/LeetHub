class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        remove_x = lambda num: abs(num - x)

        arr.sort(key=remove_x)
        result = arr[:k]

        result.sort()
        return result
