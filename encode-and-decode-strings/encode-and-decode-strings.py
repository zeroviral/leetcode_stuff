class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        self.last = strs
        return "".join(self.last)
        

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        return self.last
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))