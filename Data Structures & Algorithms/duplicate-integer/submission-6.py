class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        for ch in nums:
            if ch in seen:
                return True
            else:
                seen.append(ch)
        return False
             
        
