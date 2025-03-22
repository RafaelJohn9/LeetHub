class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        def insert_zero(arr: List[int], index: int):
            """
            Inserts zero at a particular index and pushes the other elemnts to the right.
            """
            n = len(arr)

            if index >= n:
                return

            temp = arr[index]
            arr[index] = 0
            index += 1

            while index < n:
                next_temp = arr[index]
                arr[index] = temp
                temp = next_temp
                index += 1
            
        
        n = len(arr)
        i = 0

        while i < len(arr):
            if arr[i] == 0:
                insert_zero(arr, i + 1)
                i += 2
                continue
            i += 1
        