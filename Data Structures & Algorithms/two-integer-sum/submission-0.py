class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_dict = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in map_dict:
                return [map_dict[diff], i]
            map_dict[num] = i
                       
            

            
            