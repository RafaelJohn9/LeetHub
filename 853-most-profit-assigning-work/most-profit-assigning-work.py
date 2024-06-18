class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()

        total_profit = 0
        jobs_index = 0
        max_profit = 0

        for ability in worker:
            while jobs_index < len(jobs) and ability >= jobs[jobs_index][0]:
                curr_profit = jobs[jobs_index][1]
                max_profit = max(max_profit, curr_profit)
                jobs_index += 1
            total_profit += max_profit
    
        return total_profit