class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        global maxScore
        maxScore = 0

        def possible_combinations(subset):
            global maxScore
            if len(subset) == 0:
                return True
            
            current_max_score = 0
            possible_letters = letters.copy()
            for word in subset:
                for letter in word:
                    if letter not in possible_letters:
                        return True
                    current_max_score = max(current_max_score, current_max_score + score[(ord(letter) - 97)])
                    del(possible_letters[possible_letters.index(letter)])
            maxScore = max(maxScore, current_max_score)
            return True

        subsets = [[]]        

        for word in words:
            temp = []
            print(subsets)
            for subset in subsets:
                new_subset = [word for word in subset]
                new_subset.append(word)
                if not possible_combinations(new_subset):
                    return maxScore
                temp.append(new_subset)
            subsets.extend(temp)
        return maxScore
