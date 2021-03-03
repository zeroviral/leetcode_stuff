class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        count = 0        
        
        for typ, color, name in items:
            
            if ruleKey == "type":
                if typ == ruleValue:
                    count += 1
            elif ruleKey == "color":
                if color == ruleValue:
                    count += 1
            else:
                if ruleValue == name:
                    count += 1
        
        return count