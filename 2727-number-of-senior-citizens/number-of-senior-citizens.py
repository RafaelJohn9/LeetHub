class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count: int = 0
        for person in details:
            if int(person[11:13]) > 60:
                count += 1
        return count