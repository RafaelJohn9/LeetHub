class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        lucky_numbers = []

        for row in range(len(matrix)):
            lucky_num = min(matrix[row])
            is_lucky_num = True
            col = matrix[row].index(lucky_num)
            for i in range(len(matrix)):
                if matrix[i][col] > lucky_num:
                    is_lucky_num = False
                    break
            if is_lucky_num:
                lucky_numbers.append(lucky_num)

        return lucky_numbers