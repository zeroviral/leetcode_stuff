class Solution:
    def average(self, salary: List[int]) -> float:
        maxSal, minSal = max(salary), min(salary)
        
        
        total = 0
        
        for pay in salary:
            if pay != maxSal and pay != minSal:
                total += pay
        
        return total / (len(salary) - 2)