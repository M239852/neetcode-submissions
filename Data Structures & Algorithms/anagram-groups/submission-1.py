class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {} ## val -> idx
        for str in strs:
            key = ''.join(sorted(str))
            hash.setdefault(key, []).append(str)
        return list(hash.values())
            
                

        