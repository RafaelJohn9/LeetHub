class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        
        i = 0
        n = len(arr)
        while i < n:
            if arr[i] == 0 and arr.count(0) == 1:
                i += 1
                
            if arr[i] * 2 <= arr[-1] and  arr[i] * 2 in arr:
                return True
            i += 1
        
        return False