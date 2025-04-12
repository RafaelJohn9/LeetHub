class Solution:
    def captureForts(self, forts: List[int]) -> int:
        def capture_forward(forts: List[int]) -> int:
            count = 0
            for fort in forts:
                if fort == 0:
                    count += 1
                elif fort == -1:
                    return count
                else:
                    return 0
            return 0

        def capture_back(forts: List[int]) -> int:
            count = 0
            n = len(forts)
            i = n - 1

            while i >= 0:
                if forts[i] == 0:
                    count += 1
                elif forts[i] == -1:
                    return count
                else:
                    return 0
                
                i -= 1
            
            return 0
        
        indexOfOne = [i for i in range(len(forts)) if forts[i] == 1]

        big_capture = 0
        for myFortIndex in indexOfOne:
            big_capture = max(big_capture, capture_forward(forts[myFortIndex + 1:]), capture_back(forts[: myFortIndex]))
        
        return big_capture
