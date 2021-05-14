class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        k_ = len(cardPoints)-k
        total = sum(cardPoints[:k_])
        minimum = total
        for i in range(len(cardPoints)-k_):
            total += cardPoints[i+k_] - cardPoints[i]
            minimum = min(minimum, total)
        return sum(cardPoints)-minimum