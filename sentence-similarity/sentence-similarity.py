class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        seen = set((word1, word2) for word1, word2 in similarPairs)
        
        for a, b in zip(sentence1, sentence2):
            if a != b and (a, b) not in seen and (b, a) not in seen:
                return False
        return True
        