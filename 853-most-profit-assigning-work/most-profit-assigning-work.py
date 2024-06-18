from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Pair difficulty with profit and sort them by difficulty
        jobs = sorted(zip(difficulty, profit))
        
        # Sort the workers by their ability
        worker.sort()
        
        max_profit = 0
        total_profit = 0
        job_index = 0
        
        # Iterate over each worker
        for ability in worker:
            # While the worker can do the job, update the max_profit
            while job_index < len(jobs) and ability >= jobs[job_index][0]:
                max_profit = max(max_profit, jobs[job_index][1])
                job_index += 1
            # Add the best possible profit for this worker to the total profit
            total_profit += max_profit
        
        return total_profit
