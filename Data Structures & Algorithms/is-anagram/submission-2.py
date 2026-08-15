class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        joined_s = "".join(sorted_s)
        sorted_t = sorted(t)
        joined_t = "".join(sorted_t)

        return joined_s == joined_t
        