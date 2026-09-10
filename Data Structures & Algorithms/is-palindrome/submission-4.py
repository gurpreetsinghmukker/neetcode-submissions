class Solution:
    def isPalindrome(self, s: str) -> bool:
        # if s.isalnum() and len(s) == 1:
        #     return True

        # char_list = []
        # for char in s:
        #     if (char>='A' and char<='z') or (char>="0" and char<="9"):
        #         char_list.append(char.lower())
        # for i, c in enumerate(char_list):
        #     if not char_list[i] == char_list[len(char_list)-1-i]:
        #         return False
        # return True
        if s.isalnum() and len(s) == 1:
            return True

        i = 0
        j = len(s) - 1
        s = s.lower()
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            
            if not s[j].isalnum():
                j -= 1
                continue
            
            if s[i] != s[j]:
                return False
            
            i += 1
            j -= 1


        return True