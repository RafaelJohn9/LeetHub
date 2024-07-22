class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Helper function to perform in-place partitioning
        def partition(low, high):
            pivot = heights[high]
            i = low - 1
            for j in range(low, high):
                if heights[j] >= pivot:  # Note the comparison is reversed for descending order
                    i += 1
                    heights[i], heights[j] = heights[j], heights[i]
                    names[i], names[j] = names[j], names[i]
            heights[i + 1], heights[high] = heights[high], heights[i + 1]
            names[i + 1], names[high] = names[high], names[i + 1]
            return i + 1

        # Helper function to perform in-place quicksort
        def quicksort(low, high):
            if low < high:
                pi = partition(low, high)
                quicksort(low, pi - 1)
                quicksort(pi + 1, high)

        quicksort(0, len(names) - 1)
        return names
