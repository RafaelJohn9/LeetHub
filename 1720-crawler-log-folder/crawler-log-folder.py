class Solution:
    def minOperations(self, logs: List[str]) -> int:
        step = 0

        for log in logs:
            if "../" == log:
                step = step - 1 if  step > 0 else 0
            else:
                step = (step + 1) if "./" != log else (step + 0)
                
        return step