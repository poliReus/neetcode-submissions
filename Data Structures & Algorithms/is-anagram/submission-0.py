class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        first = Counter(s)
        second = Counter(t)
        if not len(s) == len(t):
            return False
        if first == second:
            return True
        else:
            return False