class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def quicksort(numbers: List[int], low: int, high: int) -> None:
            if low < high:
                pi = partition(numbers, low, high)
                quicksort(numbers, low, pi - 1)
                quicksort(numbers, pi + 1, high)

        def partition(numbers: List[int], low: int, high: int) -> int:
            pivot = numbers[high]
            i = low - 1
            for j in range(low, high):
                if numbers[j] < pivot:
                    i += 1
                    numbers[i], numbers[j] = numbers[j], numbers[i]
            numbers[i + 1], numbers[high] = numbers[high], numbers[i + 1]
            return i + 1

        quicksort(nums, 0, len(nums) - 1)