class Solution:
    def tribonacci(self, n: int) -> int:
        base_sequence = [0, 1, 1]

        while n + 1 > len(base_sequence):
            lastnum = len(base_sequence) - 1
            next_num = base_sequence[lastnum] + base_sequence[lastnum - 1] + base_sequence[lastnum - 2]
            base_sequence.append(next_num)

        return base_sequence[n]