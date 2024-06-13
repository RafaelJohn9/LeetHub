class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        count = 0
        for seat, student in zip(seats, students):
            count += abs(seat - student)

        return count