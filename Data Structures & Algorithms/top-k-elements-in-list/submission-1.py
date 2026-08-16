class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {} ## hash
        for num in nums:
            hash.setdefault(num, 0)
            hash[num] = hash[num] + 1 
        sorted_pairs = sorted(hash.items(), key = lambda x: x[1], reverse = True)
        new_list = [pair[0] for pair in sorted_pairs[:k]]
        return new_list
       
        

            

        
            