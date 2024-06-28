class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        ord_of_importance = {}

        for road in roads:
            for city in road:
                if ord_of_importance.get(city, None):
                    ord_of_importance[city] += 1
                else:
                    ord_of_importance[city] = 1

        order = sorted(zip(ord_of_importance.values(), ord_of_importance.keys()), reverse=True)

        indicator = n
        for i in range(1, len(ord_of_importance)+ 1):
            ord_of_importance[order[i - 1][1]] = indicator
            indicator -= 1
        
        total_importance = 0

        for road in roads:
            total_importance += (ord_of_importance[road[0]] + ord_of_importance[road[1]])

        return total_importance