class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n: int = len(code)
        result: List[int] = code.copy()

        def get_new_value(i: int, iterator: int) -> int:
            nonlocal n
            _sum: int = 0
            step = 0

            i += iterator
            while step != k:
                if i >= n:
                    i = 0
                
                _sum += code[i]
                i += iterator
                step += iterator
            
            return _sum
        
        iterator: int = 1

        if k < 0:
            iterator = -1

        i: int = 0
        while i < n:
            result[i] = get_new_value(i, iterator)
            i += 1
        
        return result
