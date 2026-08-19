class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = 2
        i = 0
        ans = []
        while i != n: 
            for ch in nums:
                ans.append(ch)
            i += 1

        
        return ans 