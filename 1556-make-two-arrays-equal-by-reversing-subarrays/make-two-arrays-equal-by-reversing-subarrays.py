class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        arr.sort()
        target.sort()

        for num, target_num in zip(arr, target):
            if num != target_num:
                return False
        return True