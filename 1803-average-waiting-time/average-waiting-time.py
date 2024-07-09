class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_customers = len(customers)
        total_order_time = 0

        total_overlap_time = 0
        time = customers[0][0]

        for arrival_time, order_time in customers:
            if arrival_time < time:
                total_overlap_time += (time - arrival_time)
            else:
                time = arrival_time

            total_order_time += order_time
            time += order_time
        return (total_order_time +  total_overlap_time) / total_customers