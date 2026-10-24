class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} # to keep track of number freq
        ret_list = [] # to keep track of top k numbers

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        ret_list = sorted(freq.keys(), key=freq.get, reverse=True)

        return ret_list[:k]
            
                
                
                