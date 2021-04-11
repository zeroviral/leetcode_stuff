class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        sets = set()
        for word1, word2 in similarPairs:
            sets.add((word1, word2))
        
        for w, v in zip(sentence1, sentence2):
            if w != v and (w,v) not in sets and (v,w) not in sets:
                return False
        return True
        