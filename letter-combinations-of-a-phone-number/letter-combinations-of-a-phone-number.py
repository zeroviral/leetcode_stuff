from collections import deque

class Solution(object): 
    def letterCombinations(self, digits):
        '''
        We need: Dictionary mapping of all digits to letters, ans array with an empty string in it.
        1. Loop through the digits from the input
            1.1. Get the list of characters that the digit maps to
            1.2. Create a temporary array that will hold the values and swap places with the answer
                1.2.1. For every character in our temporary array
                    1.2.1.1. We will append each character to each value in our original array
            1.3. Make ans = temp array.
        2. Return the ans array.
        '''
        if digits == "": return []
        lookup = {
            "1":"", 
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
            "10":" "
        }
        ans = [""]
        
        for digit in digits:
            new = []
            for c in lookup[digit]:
                for val in ans:
                    new.append(val + c)
            ans = new
        return ans