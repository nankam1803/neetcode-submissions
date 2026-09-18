class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map_dict = {}

        for num in nums:
            if num in map_dict:
                return True

            map_dict[num] = num
        
        return False