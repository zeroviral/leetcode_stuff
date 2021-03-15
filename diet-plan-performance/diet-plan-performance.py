class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        currSum = sum(calories[:k])
        
        if currSum < lower:
            total = -1
        elif currSum > upper:
            total = 1
        else:
            total = 0
            
        for i in range(k, len(calories)):
            currSum += -calories[i - k] + calories[i]
            if currSum < lower:
                total -= 1
            elif currSum > upper:
                total += 1
        
        return total
            