class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        zeros = arr.count(0)  # Count the number of zeros to be duplicated
        i = n - 1
        j = n + zeros - 1  # Logical extended array index

        # Iterate backwards and shift elements
        while i >= 0:
            if j < n:
                arr[j] = arr[i]
            
            j -= 1
            
            if arr[i] == 0:  # Duplicate zero
                if j < n:
                    arr[j] = 0
                j -= 1
            
            i -= 1