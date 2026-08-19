class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i, n in enumerate(nums):
            diff = target - n ## nums[j] or diff = target - nums[i]
            if diff in hash: 
                return [hash[diff], i]
            hash[n] = i
            