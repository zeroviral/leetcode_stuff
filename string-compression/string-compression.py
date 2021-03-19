from collections import Counter

class Solution:
    def compress(self, chars: List[str]) -> int:
        p1, p2 = 0, 0
        while p2 < len(chars):
		
            chars[p1] = chars[p2]
            count = 1
			
            # While the value of p2 is less than the length AND the value is the same as the next element,
            # increment p2 and our count. Keep the status quo.
            while p2 + 1 < len(chars) and chars[p2] == chars[p2 + 1]:
                p2 += 1
                count += 1
			
            # If our count is greater than 1, there's a possiblity there's 2 digits.
            if count > 1:
                for element in str(count):
                    chars[p1 + 1] = element
                    p1 += 1
            p1 += 1
            p2 += 1
        
        return p1
        
        