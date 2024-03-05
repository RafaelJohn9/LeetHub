class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str = list(map(str, digits))
        num = int(''.join(num_str))
        num += 1
        num = list(str(num))
        return list(map(int, num))