class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 3:
            return 1

        magical_str = [1, 2, 2]

        i = 2
        num = 1

        while len(magical_str) < n:
            count = magical_str[i]
            magical_str.extend([num]* count)
            num = 3 - num
            i += 1

        partial_str = magical_str[:n]

        return partial_str.count(1)