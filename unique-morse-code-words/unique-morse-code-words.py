class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        '''
        1. Create a dictionary of the mappings of morse code to the letters.
        2. Create a dictionary that will hold the frequency of the morse code combination
        3. Iterate for each word in words
            3.1. For each char in each word, you will use a temp string and append the morse code value of it.
            3.2. At the end of the inner for loop, we will add one to the dictionary mapping of the morse code.
        4. Return the sum of all values within the second dictionary (frequency dictionary)
        '''
        lookup = {
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": ".-..",
            "m": "--",
            "n": "-.",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "-.--",
            "z": "--.."
        }
        freq = collections.defaultdict(int)
        
        for word in words:
            temp = ""
            for c in word:
                temp += lookup[c]
            freq[temp] += 1
            
        return len(freq)
        
        