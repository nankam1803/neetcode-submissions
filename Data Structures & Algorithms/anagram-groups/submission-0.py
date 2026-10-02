class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        outer_list = defaultdict(list)  # Create an defaultdic to store final values and handle edge cases

        for string in strs:
            count = [0] * 26 # Initializing list of 26 zeros for each string (a-z)

            for i in string:
                count[ord(i)-ord("a")] += 1 # Mapping letter to 0-26. ASCII(Curr)-ASCII(A)

            outer_list[tuple(count)].append(string) # Appending all 'string' to same 'count' keys

        return list(outer_list.values()) # Return normal list values
            