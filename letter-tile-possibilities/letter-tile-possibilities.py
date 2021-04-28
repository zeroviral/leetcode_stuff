class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        seqs = set()
        visits = [0] * len(tiles)

        def dfs(seq: str, depth: int):
            if seq:
                print(f'Adding: {seq}')
                seqs.add(seq)
            
            if depth == len(tiles):
                return

            for i in range(len(tiles)):
                if not visits[i]:
                    visits[i] += 1
                    dfs(seq + tiles[i], depth + 1)
                    visits[i] -= 1

        dfs('', 0)
        return len(seqs)
    
    '''
    
    Input: AAB
    visited = [0, 1, 0]
    
    combos = (A, AA, AAB, AB)
    seq = "A"
    '''