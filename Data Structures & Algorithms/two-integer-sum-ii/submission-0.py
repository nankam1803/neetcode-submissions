class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map_dict = {}

        for i, num in enumerate(numbers):
            diff = target - num
            if diff in map_dict:
                return [map_dict[diff]+1, i+1]
            map_dict[num] = i