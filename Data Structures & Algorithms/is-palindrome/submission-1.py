class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_list = ''.join([char.lower() for char in s if char.isalnum()])

        for i in range(len(str_list)):
            left = str_list[i]
            right = str_list[-1-i]

            if left != right:
                return False
            
        return True
            

