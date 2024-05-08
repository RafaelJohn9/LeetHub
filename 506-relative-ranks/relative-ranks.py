class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = score.copy()
        sorted_score.sort(reverse=True)  # Sorting the copied list in descending order
        result = [0] * len(score)

        for i in range(len(score)):
            if i == 0:
                index = score.index(sorted_score[i])
                result[index] = "Gold Medal"
            elif i == 1:
                index = score.index(sorted_score[i])
                result[index] = "Silver Medal"
            elif i == 2:
                index = score.index(sorted_score[i])
                result[index] = "Bronze Medal"
            else:
                rank = i + 1
                index = score.index(sorted_score[i])
                result[index] = str(rank)

        return result
