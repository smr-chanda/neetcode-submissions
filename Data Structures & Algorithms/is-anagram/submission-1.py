class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = sorted(list(s))
        list_t = sorted(list(t))
        if sorted(list(s)) == sorted(list(t)):
            return True
        return False

        